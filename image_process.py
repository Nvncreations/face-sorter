import face_recognition as fr
import sys

def image_load(path:str,jitter):
    image=fr.load_image_file(path,mode='RGB')
    try:
        image_encoding = fr.face_encodings(image,num_jitters=jitter)[0]
    except IndexError:
        sys.exit('program exited due to no face found in provided image')
    return image_encoding

def image_load_faces(path:str,num_jitters=1,upsample=1):
    
    image = fr.load_image_file(path)
        # Find all faces in the current image
    face_locations = fr.face_locations(image,number_of_times_to_upsample=upsample)
    face_encodings = fr.face_encodings(image, face_locations,num_jitters=num_jitters)
    return face_encodings

def face_compare(ref_face,face_encode,tolerance):
     match = fr.compare_faces([ref_face], face_encode,tolerance=tolerance)
     return match[0]
