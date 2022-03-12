import glob
import os
import time
import shutil
print("Checking existence of Topaz model files")
path_to_temp = 'Your path to Temp folder (%Temp%)'
path_to_our_folder = 'Path to destination folder'
os.chdir(path_to_temp)
while True:
    for file in glob.glob("*.xml") + glob.glob("*.bin") + glob.glob("*.onnx"):
        print(file)
        try:
            shutil.copy2(file, path_to_our_folder+file)
        except:
            print("Something went wrong with file: "+file)
    time.sleep(0.5)


