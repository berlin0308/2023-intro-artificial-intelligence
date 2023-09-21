import os

def rename_folder_jpg(folder_path):
    jpg_files = [f for f in os.listdir(folder_path) if f.endswith('.jpg')]
    for i, jpg_file in enumerate(jpg_files, start=1):
        new_name = f'image_{i:03d}.jpg'
        
        old_path = os.path.join(folder_path, jpg_file)
        new_path = os.path.join(folder_path, new_name)
        
        os.rename(old_path, new_path)
        print(f'Renamed: {jpg_file} -> {new_name}')

def rename_folder_wav(folder_path):
    wav_files = [f for f in os.listdir(folder_path) if f.endswith('.wav')]
    for i, wav_file in enumerate(wav_files, start=1):
        new_name = f'audio_{i:03d}.wav'
        
        old_path = os.path.join(folder_path, wav_file)
        new_path = os.path.join(folder_path, new_name)
        
        os.rename(old_path, new_path)
        print(f'Renamed: {wav_file} -> {new_name}')


root_folder = "./Dog/"
rename_folder_wav(root_folder)
