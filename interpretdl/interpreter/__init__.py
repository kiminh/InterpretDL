
from .lime import LIMEInterpreter
from .gradient_cam import GradCAMInterpreter
from .integrated_gradients import IntGradInterpreter
from .smooth_grad import SmoothGradInterpreter
from .occlusion import OcclusionInterpreter
from .gradient_shap import GradShapInterpreter

__all__ = [
    "LIMEInterpreter", "GradCAMInterpreter",
    "IntGradInterpreter", "SmoothGradInterpreter", "OcclusionInterpreter",
    "GradShapInterpreter"
]

try:
    import paddle
    from . import lime_prior
    from .lime_prior import LIMEPriorInterpreter
    from .forgetting_events import ForgettingEventsInterpreter
    __all__.append("LIMEPriorInterpreter")
    __all__.append("ForgettingEventsInterpreter")
except ModuleNotFoundError:
    print("Warning: Paddle should be installed before using LIMEPriorInterpreter or ForgettingEventsInterpreter.")
