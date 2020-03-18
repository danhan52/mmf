# Copyright (c) Facebook, Inc. and its affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#

from pythia.common.registry import registry
from pythia.datasets.vqa.vqa2.builder import VQA2Builder
from pythia.datasets.reasoning.mmimdb.dataset import MMIMDbDataset


@registry.register_builder("mmimdb")
class MMIMDbBuilder(VQA2Builder):
    def __init__(self):
        super().__init__()
        self.dataset_name = "mmimdb"
        self.dataset_class = MMIMDbDataset
