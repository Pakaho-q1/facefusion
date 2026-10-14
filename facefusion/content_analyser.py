from functools import lru_cache
from typing import List, Tuple

import numpy
from tqdm import tqdm

import facefusion.choices
from facefusion import inference_manager, state_manager, translator, video_manager
from facefusion.common_helper import is_macos
from facefusion.download import conditional_download_hashes, conditional_download_sources, resolve_download_url
from facefusion.execution import has_execution_provider
from facefusion.filesystem import resolve_relative_path
from facefusion.thread_helper import conditional_thread_semaphore
from facefusion.types import Detection, DownloadScope, DownloadSet, Fps, InferencePool, InferenceProvider, ModelSet, VisionFrame
from facefusion.vision import detect_video_fps, fit_contain_frame, is_vision_frame, read_image

STREAM_COUNTER = 0


@lru_cache()
def create_static_model_set(download_scope : DownloadScope) -> ModelSet:
	# NSFW disabled: no models, no download, no VRAM
	return {}


def get_inference_pool() -> InferencePool:
	# NSFW disabled: never load models into VRAM
	return {}


def clear_inference_pool() -> None:
	# NSFW disabled: nothing to clear
	return


def override_inference_providers() -> List[InferenceProvider]:
	if is_macos() and has_execution_provider('coreml'):
		return [ facefusion.choices.execution_provider_set.get('cpu') ]

	return []


def collect_model_downloads() -> Tuple[DownloadSet, DownloadSet]:
	# NSFW disabled: no downloads
	return {}, {}


def pre_check() -> bool:
	# NSFW disabled: always pass, no download
	return True


def analyse_stream(vision_frame : VisionFrame, video_fps : Fps) -> bool:
	# NSFW disabled: never block stream
	return False


def analyse_frame(vision_frame : VisionFrame) -> bool:
	# NSFW disabled: never flag
	return False


@lru_cache()
def analyse_image(image_path : str) -> bool:
	# NSFW disabled: skip image read entirely
	return False


@lru_cache()
def analyse_video(video_path : str, trim_frame_start : int, trim_frame_end : int) -> bool:
	# NSFW disabled: skip video decode entirely
	return False


def detect_nsfw(vision_frame : VisionFrame) -> bool:
	# NSFW disabled
	return False


def detect_with_nsfw_1(vision_frame : VisionFrame) -> bool:
	return False


def detect_with_nsfw_2(vision_frame : VisionFrame) -> bool:
	return False


def detect_with_nsfw_3(vision_frame : VisionFrame) -> bool:
	return False


def forward_nsfw(vision_frame : VisionFrame, model_name : str) -> Detection:
	# NSFW disabled: should never be called
	raise RuntimeError('NSFW model is disabled')


def prepare_detect_frame(temp_vision_frame : VisionFrame, model_name : str) -> VisionFrame:
	# NSFW disabled: should never be called
	raise RuntimeError('NSFW model is disabled')
