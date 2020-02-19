
import os, sys
import time
import multiprocessing, threading
import logging
import turtle

# current file's path
fpath = os.path.dirname(os.path.abspath(__file__))

def extname(fname):
    fa = os.path.splitext(fname)
    if len(fa) > 1:
        return fa[1].lower()
    else:
        return ""


def filename(fname):
    return os.path.split(fname)[1]


def loadModule(mpath):
    # get module's name
    moduleName = os.path.splitext(os.path.split(mpath)[1])[0]

    # try load module
    try:
        # for Python 3.5+
        import importlib.util
        spec = importlib.util.spec_from_file_location(moduleName, mpath)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        return module
    except Exception as e:
        logging.error("Can not load module %s, error msg: %s" % (mpath, str(e)))
        return None


def getScriptList(fp):
    fl = os.listdir(fp)
    fileList = [f for f in fl if extname(f) == ".py"]
    fileList.sort()
    return fileList


class RunScript:
    def __init__(self, fname, txtfile):
        self.p = None
        self.fname = fname
        self.txtfile = txtfile

        self.finished = False

    def runScript_(self):
        mod = loadModule(self.fname)
        if mod:
            # create
            ts = threading.Thread(target=self.saveRes)
            ts.start()

            # call `draw` function
            print(">>> load module: %s" % filename(self.fname))
            f = getattr(mod, "draw")
            f()

            # regist timer function, and do mainloop
            turtle.ontimer(self.drawFinished, 0)
            turtle.mainloop()

    def drawFinished(self):
        print("- draw finished!")
        self.finished = True

    def saveRes(self):
        while not self.finished:
            time.sleep(0.5)

        time.sleep(5)

        # do snapshot
        imgPath = os.path.join(fpath, "images")
        fbaseName = os.path.splitext(os.path.split(self.fname)[1])[0]
        imgName = fbaseName + ".png"
        imgFP = os.path.join(imgPath, imgName)

        cmd = 'shutter -e --min_at_startup --window="Python Turtle Graphics" -o "%s"' % imgFP
        print("cmd: ", cmd)
        os.system(cmd)

        # do markdown text output
        cfname = "codes/" + os.path.split(self.fname)[1]
        imgname = "images/" + imgName
        mt = """code: [%s](%s)\n![%s](%s)\n\n""" % (fbaseName, cfname, fbaseName, imgname)

        f = open(self.txtfile, "at")
        f.write(mt)
        f.close()

        # close drawing window
        turtle.bye()

        print("- capture finished!")

    def runScript(self):
        self.p = multiprocessing.Process(name="run_script", target=self.runScript_)
        self.p.start()
        self.p.join()

        print("- script run finished!\n\n")

if __name__ == "__main__":
    # code path
    codePath = os.path.join(fpath, "codes")
    mtfile = os.path.join(fpath, "gallery.md")

    # get code list
    if len(sys.argv) > 1:
        cl = sys.argv[1:]
    else:
        cl = getScriptList(codePath)

    print("code list: ", cl)
    print("")

    # run codes
    for c in cl:
        s = RunScript(os.path.join(codePath, c), mtfile)
        s.runScript()
