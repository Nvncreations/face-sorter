# face_sorter

A cli tool to seperate images containing provided face 

 <a href="https://github.com/skycreeds/face_sorter/issues">Request Feature</a>
  </p>
</p>

![Contributors](https://img.shields.io/github/contributors/skycreeds/face_sorter?color=dark-green) ![Forks](https://img.shields.io/github/forks/skycreeds/face_sorter?style=social) ![Stargazers](https://img.shields.io/github/stars/skycreeds/face_sorter?style=social) ![Issues](https://img.shields.io/github/issues/skycreeds/face_sorter) ![License](https://img.shields.io/github/license/skycreeds/face_sorter) 



## Installation

#pip installation

```python
   pip3 install git+https://github.com/skycreeds/face_sorter.git
```

## Usage/Examples

#Usage
```bash
flags :
    --face_pic:provide path of image with a single face_pic

    --folder_in: provide path of folder to work on (contain images in jpg or png) default is current directory

    --folder_out: provide path to folder to hold out put.Default is current directory

    --tolerence: accuracy of recognition(smaller is better but intensive) range(0,1) 0.5 is best 

    --encode_resample:times to resample face encodings(lager is better but intensive) integer, default 1
    
    --location_resample:times to resample face locations(larger better but intensive) integer, default 1
```

#Example
```bash
    face_sorter --face_pic face.jpeg --folder_in '/sample' --folder_out 'out/' --tolerence 0.5 --encode_resample 2 --location_resample 2

```




## Alert


Use tolerence,encode_resample,location_resample while keeping ram in mind.Lower tolerence,higher resampling uses more ram and can crash.
using default will be most advisable.
## License

[MIT](https://choosealicense.com/licenses/mit/)


## Authors

- [@skycreeds](https://www.github.com/skycreeds)

