CUDA_VISIBLE_DEVICES=1 python train.py --backbone xception --lr 0.007 --workers 4 --epochs 500 --batch-size 4 --gpu-ids 0 --checkname deeplab-xception --eval-interval 1 --dataset kitti \
--resume run/kitti/deeplab-xception/model_best.pth.tar
