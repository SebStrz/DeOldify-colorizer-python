import importlib.util
import subprocess
import sys
from pathlib import Path
import urllib.request

def is_package_inst(name):
    return importlib.util.find_spec(name) is not None
is_array = False

packages_required = ["fastai","torch"]
render_factor = 20

if len(sys.argv) > 1:
    if len(sys.argv) > 2:
        render_factor = int(sys.argv[2])
        print(render_factor)
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
            raise ValueError('Provide an image url and try again.')

    else:
        raise ValueError('Provide an image url and try again.')

else:
    raise ValueError('Provide an image url and try again.')

model_dir = Path('src/models')
model_dir.mkdir(parents=True, exist_ok=True)
model_dir_path = model_dir / 'ColorizeArtistic_gen.pth'

if not model_dir_path.exists():
    print("Pobieram model...")
    urllib.request.urlretrieve(
        "https://data.deepai.org/deoldify/ColorizeArtistic_gen.pth",
        model_dir_path
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
colorizer = get_image_colorizer(root_folder=Path("./src"),artistic=True)

watermarked = False#@param {type:"boolean"}

if is_array:
    for file in source_path:
        result_path = colorizer.plot_transformed_image(
            path=file,
            render_factor=render_factor,
            results_dir=Path("src/wyniki"),
            post_process=True,
            watermarked=False
        )
        print("zdjęcie pokolorowane jest pod adresem:"+str(result_path)+":")

elif source_path is not None and source_path !='':
    result_path = colorizer.plot_transformed_image(
        path=source_path,
        render_factor=render_factor,
        results_dir=Path("src/wyniki"),
        post_process=True,
        watermarked=False
    )
    print("zdjęcie pokolorowane jest pod adresem:"+str(result_path)+":")
else:
    raise ValueError('Provide an image url and try again.')
