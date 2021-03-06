import sys
sys.path.append('..')

from interpretdl import LIMEPriorInterpreter
from tutorials.assets.resnet import ResNet101
from interpretdl.data_processor.readers import get_typical_dataset_info
import glob


def lime_gp_example():
    def paddle_model(image_input):
        import paddle.fluid as fluid

        class_num = 1000
        model = ResNet101()
        logits = model.net(input=image_input, class_dim=class_num)

        probs = fluid.layers.softmax(logits, axis=-1)
        return probs

    # The model can be downloaded from
    # http://paddle-imagenet-models-name.bj.bcebos.com/ResNet101_pretrained.tar
    # More pretrained models can be found in
    # https://github.com/PaddlePaddle/models/tree/release/1.8/PaddleCV/image_classification
    trained_model = "assets/ResNet101_pretrained"

    # a list of files for preparing the LIMEPriorInterpreter
    # The ImageNet validation set (original 50K images, but 1K images here) is used,
    # users should download from http://www.image-net.org/challenges/LSVRC/2012/.
    dataset_dir = "assets/ILSVRC2012_images_val/val"
    image_paths = glob.glob(dataset_dir + "/*")
    image_paths = image_paths[:1000]

    limegp = LIMEPriorInterpreter(
        paddle_model, trained_model, prior_method="ridge")
    limegp.interpreter_init(
        image_paths, batch_size=100, weights_file_path="assets/gp_weights.npy")
    lime_weights = limegp.interpret(
        image_paths[0],
        num_samples=1000,
        batch_size=100,
        save_path='assets/lime_gp.png',
        prior_reg_force=1.0)


if __name__ == '__main__':
    lime_gp_example()
