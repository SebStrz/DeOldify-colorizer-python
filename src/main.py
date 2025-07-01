import importlib.util
import subprocess
import sys
from pathlib import Path
import urllib.request

def is_package_inst(name):
    return importlib.util.find_spec(name) is not None
is_array = False

packages_required = ["fastai","torch"]
if len(sys.argv) > 1:
    source_path = Path(sys.argv[1])
    print(source_path)
    if source_path.is_file():
        source_path = sys.argv[1]
        print("plik")
    elif source_path.is_dir():
        print("folder")
        dir = source_path
        source_path = []
        for file in dir.iterdir():
            if file.suffix.lower() in [".jpg",".png",".webp"]:
                source_path.append(file)
                is_array = True
        print(source_path)
        if not is_array:
            print("podaj ścieżkę do zdjęcia")
            source_path = input()
    else:
        print("podaj ścieżkę do zdjęcia")
        source_path = input()
else:
    print("podaj ścieżkę do zdjęcia")
    source_path = input()
#for pcg in packages_required:
#    if not is_package_inst(pcg):
#        print(pcg)
#        #subprocess.run([sys.executable, "-m","pip","install","-r","requirements-colab.txt"],check=True)

model_dir = Path('./models')
model_dir.mkdir(parents=True, exist_ok=True)
model_path = model_dir / 'ColorizeArtistic_gen.pth'

if not model_path.exists():
    print("Pobieram model...")
    urllib.request.urlretrieve(
        "https://data.deepai.org/deoldify/ColorizeArtistic_gen.pth",
        model_path
    )
    print("Model pobrany.")

from deoldify import device
from deoldify.device_id import DeviceId

device.set(device=DeviceId.GPU0)

import torch

if not torch.cuda.is_available():
    print('GPU not available.')

import warnings

warnings.filterwarnings("ignore")

import fastai
from deoldify.visualize import *
colorizer = get_image_colorizer(artistic=True)

render_factor = 20#@param {type: "slider", min: 7, max: 40}
watermarked = False#@param {type:"boolean"}

if is_array:
    for file in source_path:
        result_path = colorizer.plot_transformed_image(
            path=file,
            render_factor=render_factor,
            results_dir=Path("./wyniki"),
            post_process=True,
            watermarked=False
        )
        print("zdjęcie pokolorowane jest pod adresem: "+str(result_path))

elif source_path is not None and source_path !='':
    result_path = colorizer.plot_transformed_image(
        path=source_path,
        render_factor=render_factor,
        results_dir=Path("./wyniki"),
        post_process=True,
        watermarked=False
    )
    print("zdjęcie pokolorowane jest pod adresem: "+str(result_path))
else:
    print('Provide an image url and try again.')
