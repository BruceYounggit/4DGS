import torch
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "5"
# 检查CUDA是否可用
if torch.cuda.is_available():
    # 获取GPU数量
    n_gpu = torch.cuda.device_count()
    print(f"Number of available GPUs: {n_gpu}")

    # 获取并打印所有可用GPU的序号和名称
    for i in range(n_gpu):
        print(f"GPU {i}: {torch.cuda.get_device_name(i)}")
else:
    print("CUDA is not available. No GPU detected.")