import numpy as np
from scipy import misc
import json, time


class data_loader(object):
	def __init__(self, data_src, metadata_src, gap = 2):
		## loading data file and metadata
		time1 = time.time()
		self.data_src = data_src
		self.metadata_src = metadata_src
		self.gap = gap
		## convert to zero centered
		self.data = np.load(data_src) - 128
		with open(metadata_src) as metadata_file:
			self.metadata = json.load(metadata_file)
		self.video_names = sorted(list(self.metadata.keys()))
		self.train_test_split()
		self.mean_image = np.mean(self.data[self.train_x_start_index, :, :, :], axis = 0)
		time2 = time.time()
		print("Data loaded! Took {:.2f} seconds".format(time2 - time1))
		print("Data Shape {}".format(self.data.shape))
		print("train: {0}   test: {1}".format(len(self.train_x_start_index), len(self.test_x_start_index)))
	
	def train_test_split(self):
		# last two videos as test
		train_index = []
		test_index = []
		train_video = list(range(len(self.metadata) - 2))
		test_video = list(range(len(self.metadata) - 2, len(self.metadata)))
		# training set
		self.train_x_start_index, self.train_x_end_index, self.train_y_index = self.generate_index(train_video)
		# test set
		self.test_x_start_index, self.test_x_end_index, self.test_y_index = self.generate_index(test_video)

	def generate_index(self, clip_indices):
	    x_start_index = []
	    x_end_index = []
	    y_index = []
	    mid_gap = self.gap //2
	    for i in clip_indices:
	        clip_list = self.metadata[self.video_names[i]]
	        start_index = list(range(0, len(clip_list) - self.gap))
	        end_index = [i + self.gap for i in start_index]
	        mid_index = [i + mid_gap for i in start_index]
	        x_start_index += [self.metadata[self.video_names[i]][j] for j in start_index]
	        x_end_index += [self.metadata[self.video_names[i]][j] for j in end_index]
	        y_index += [self.metadata[self.video_names[i]][j] for j in mid_index]
	    return (x_start_index, x_end_index, y_index)

	def get_batch(self, indices, training = True):
		### getting a batch of data with desinated indices
		if training:
			start_indices = np.asarray([self.train_x_start_index[i] for i in indices])
			end_indices = np.asarray([self.train_x_end_index[i] for i in indices])
			mid_indices = np.asarray([self.train_y_index[i] for i in indices])
		else:
			start_indices = np.asarray([self.test_x_start_index[i] for i in indices])
			end_indices = np.asarray([self.test_x_end_index[i] for i in indices])
			mid_indices = np.asarray([self.test_y_index[i] for i in indices])
		start_frames = self.data[start_indices, :, :, :]
		end_frames = self.data[end_indices, :, :, :]
		X_batch = np.concatenate([start_frames, end_frames], axis = 3)
		y_batch = self.data[mid_indices, :, :, :]
		return(X_batch, y_batch)

	def get_minibatches(self, minibatch_size = 16, training=True):
		"""
		Iterates through the provided data one minibatch at at time. You can use this function to
		iterate through data in minibatches for ONE epoch:
		    for batch_x, batch_y in get_minibatches(inputs, minibatch_size):
		        train on this batch...
		"""
		if training:
			cur_start_idx = self.train_x_start_index
			cur_end_idx = self.train_x_end_index
			cur_y_idx = self.train_y_index
			data_size = len(self.train_x_start_index)
		else:
			cur_start_idx = self.test_x_start_index
			cur_end_idx = self.test_x_end_index
			cur_y_idx = self.test_y_index
			data_size = len(self.test_x_start_index)
		for minibatch_start in np.arange(0, data_size, minibatch_size):
			start = minibatch_start
			end = minibatch_start + minibatch_size
			yield self.minibatch(start, end, cur_start_idx, cur_end_idx, cur_y_idx)

	def minibatch(self, start, end, start_idx, end_idx, mid_idx):
		left_frame = np.asarray(start_idx[start:end])
		right_frame = np.asarray(end_idx[start:end])
		mid_frame = np.asarray(mid_idx[start:end])
		X = np.concatenate([self.data[left_frame, :, :, :], self.data[right_frame, :, :, :]], axis = 3)
		y = self.data[mid_frame, :, :, :]
		return(X, y)
	




		
