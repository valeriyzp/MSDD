from Tools.SingletonMeta import SingletonMeta
from Model.VGGNet import VGGNet
from Settings.DefaultSettings import DefaultSettings


class ModelsKeeper(metaclass=SingletonMeta):

    def __init__(self):
        self.models = {
            "VGG11": VGGNet("VGG11", DefaultSettings.VGG11_PATH),
            "VGG11 LRN": VGGNet("VGG11_LRN", DefaultSettings.VGG11_LRN_PATH),
            "VGG13": VGGNet("VGG13", DefaultSettings.VGG13_PATH),
            "VGG16": VGGNet("VGG16", DefaultSettings.VGG16_PATH),
            "VGG16 1": VGGNet("VGG16_1", DefaultSettings.VGG16_1_PATH),
            "VGG19": VGGNet("VGG19", DefaultSettings.VGG19_PATH),
        }

        for name, model in self.models.items():
            if model.is_saved_fitted_model():
                model.load_model_info()

    def get_models(self):
        return self.models

    def get_model_by_name(self, model_name):
        if model_name in self.models.keys():
            return self.models[model_name]
        else:
            return None
