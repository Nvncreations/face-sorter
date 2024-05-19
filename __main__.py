import argparse
import os
from tqdm import tqdm
from face_sorter.image_process import image_load,image_load_faces,face_compare
from face_sorter.folder_process import file_copy

def main():
    
    parser = argparse.ArgumentParser(description='face_sorter')
    parser.add_argument('--face_pic', type=str, help='face')
    parser.add_argument('--folder_in', type=str, help='folder to search')
    parser.add_argument('--folder_out',type=str,help='folder for output inages')
    parser.add_argument('--tolerence',type=float,help='accuracy of recognition(smaller is better but intensive)')
    parser.add_argument('--encode_resample',type=int,help='times to resample face encodings(lager is better but intensive)')
    parser.add_argument('--location_resample',type=int,help='times to resample face locations(larger better but intensive)')
    args = parser.parse_args()
    
    #if face_pic is provided
    if args.face_pic:
        if args.tolerence is None:
            tol=0.5
        else:
            tol=args.tolerence

        if args.encode_resample is None:
            jit=1
        else:
            jit=args.encode_resample

        if args.location_resample is None:
            up=1
        else:
            up=args.location_resample


        
        #load face
        ref_face=image_load(args.face_pic,jitter=jit)

        #check if user provided path for folder to check
        if args.folder_in:
            cdir=args.folder_in
        else:
            #take current folder
            cdir=os.getcwd()
        
        if args.folder_out:
            out_dir=args.folder_out
        else:
            #take current folder
            try:
                os.mkdir('out')
            except FileExistsError:
                pass
            out_dir=os.getcwd()+'/out'

        for filename in tqdm(os.listdir(cdir)):
            
            if filename.endswith(".jpg") or filename.endswith(".png")or filename.endswith('.JPG'):
                face_encode=image_load_faces(cdir+'/'+filename,num_jitters=jit,upsample=up)
                for face_encoding in face_encode:
                    match = face_compare(ref_face,face_encoding,tolerance=tol)
                    if match:
                        print(filename)
                        file_copy(srs=(cdir+'/'+filename),dat=out_dir,file=filename)
    else:
        print('face to sort not entered')
        

                        
                


                

        

        
        

        










    

if __name__ == '__main__':
    main()