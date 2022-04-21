from ast import literal_eval
from pathlib import Path

from src.config.config import Config


class SpeechConfig(Config):

    DATA_DIR = 'data/speech'

    DATASET_DIR = Path(DATA_DIR)/'dataset'
    VOCAB_DIR = Path(DATA_DIR)/'vocab'

    CHAR_VOCAB_FILE = Path(VOCAB_DIR)/'char.txt'
    # CHAR_VOCAB_FILE = Path("./")/'combined_char.txt'
    # FONT_VOCAB_FILE = Path(VOCAB_DIR)/'font.txt'

    # IMAGE_DIR = Path(DATA_DIR)/'image_64'
    IMAGE_DIR = Path(DATA_DIR)/'speech'
    EXP_DIR = Path('out/handwriting')

    # TXT_DATASET = Path(DATASET_DIR)/'text.csv'
    # IMG_DATASET = Path(DATASET_DIR)/'image.csv'
    IMG_TXT_DATASET = Path(DATASET_DIR)/'speech_text.csv'

    TRAIN_DATASET = Path(DATASET_DIR)/'train.csv'
    EVAL_DATASET = Path(DATASET_DIR)/'eval.csv'
    TEST_DATASET = Path(DATASET_DIR)/'test.csv'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.mixed_precision_training = kwargs.pop('mixed_precision_training', False)

        # self.txt_batch_size = kwargs.pop('txt_batch_size', 12)
        # self.img_batch_size = kwargs.pop('img_batch_size', 12)
        self.speech_txt_batch_size = kwargs.pop('speech_txt_batch_size', 12)
        # self.batch_size = self.txt_batch_size + self.img_batch_size + self.img_txt_batch_size
        self.batch_size = self.img_txt_batch_size
        self.iter_dataset_index = kwargs.pop('iter_dataset_index', 0)

        self.max_char_len = kwargs.pop('max_char_len', 128)
        self.bleu_score_ngram = kwargs.pop('bleu_score_ngram', 16)
        self.bleu_score_weights = [1/self.bleu_score_ngram] * self.bleu_score_ngram

    def update_batch_size(self, device_count):
        if device_count:
            self.txt_batch_size *= device_count
            self.img_batch_size *= device_count
            self.img_txt_batch_size *= device_count
            self.batch_size *= device_count
