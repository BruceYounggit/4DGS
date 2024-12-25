import os
import shutil
datadir = '/mnt/d/yunfei-174/FourDGaussian/data/multipleview/pkuCrowd'
# #下面这循环是为了删除多余的文件夹
# for folder_name in sorted(os.listdir(datadir)):
#     # camera folder should be named as 'cam_00', 'cam_01', ...
#     if not folder_name.startswith('cam_'):
#         continue
#     if len(folder_name) != 6:
#         # replace 'cam_0' with 'cam_00'
#         new_folder_name = 'cam_0' + folder_name[-1]
#         os.rename(os.path.join(datadir, folder_name), os.path.join(datadir, new_folder_name))
#         folder_name = new_folder_name
#
#     for folder2 in os.listdir(os.path.join(datadir, folder_name)):
#         if folder2 != 'images' and not folder2.endswith('png'):
#             if os.path.isdir(os.path.join(datadir, folder_name, folder2)):
#                 shutil.rmtree(os.path.join(datadir, folder_name, folder2))
#             elif os.path.isfile(os.path.join(datadir, folder_name, folder2)):
#                 os.remove(os.path.join(datadir, folder_name, folder2))
#             else:
#                 print('unknown file type')
#         elif folder2.endswith('png'):
#             continue
#         else:
#             # move all images to the parent directory
#             for fname in os.listdir(os.path.join(datadir, folder_name, folder2)):
#                 os.rename(os.path.join(datadir, folder_name, folder2, fname), os.path.join(datadir, folder_name, fname))
#                 print(f'Finished processing {folder_name}')
#             shutil.rmtree(os.path.join(datadir, folder_name, folder2))
#         print(f'{folder_name} done.')

# 将所有帧由"000000.png"改为"frame_00000.png"格式
# for cam_fold in sorted(os.listdir(datadir)):
#     for frame_file in sorted(os.listdir(os.path.join(datadir, cam_fold))):
#         if frame_file.endswith('.png'):
#             new_frame_file = 'frame_' + frame_file[1:]
#             os.rename(os.path.join(datadir, cam_fold, frame_file), os.path.join(datadir, cam_fold, new_frame_file))
#             print(f'Finished processing {frame_file}')
#     print(f'{cam_fold} done.')

for cam_fold in sorted(os.listdir(datadir)):
    # 去掉cam_fold中间的下划线
    new_cam_fold=cam_fold.replace('_','')
    os.rename(os.path.join(datadir, cam_fold), os.path.join(datadir, new_cam_fold))