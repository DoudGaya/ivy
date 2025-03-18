ALL_TORCH_FRONTEND_FUNCTIONS = {
    "torch": [
        "abs",
        "absolute",
        "acos",
        "acosh",
        "add",
        "addbmm",
        "addcdiv",
        "addcmul",
        "addmm",
        "addmv",
        "addr",
        # "adjoint",
        "all",
        "allclose",
        "amax",
        "amin",
        # "aminmax",
        "angle",
        "any",
        "arange",
        # "arccos",
        # "arccosh",
        # "arcsin",
        # "arcsinh",
        # "arctan",
        "arctan2",
        "arctanh",
        "argmax",
        "argmin",
        # "argsort",
        # "argwhere",
        "as_strided",
        "as_tensor",
        # "asarray",
        "asin",
        # "asinh",
        "atan",
        "atan2",
        "atanh",
        # "atleast_1d",
        # "atleast_2d",
        # "atleast_3d",
        "baddbmm",
        # "bartlett_window",
        "bernoulli",
        "bincount",
        "bitwise_and",
        # "bitwise_left_shift",
        "bitwise_not",
        "bitwise_or",
        # "bitwise_right_shift",
        "bitwise_xor",
        # "blackman_window",
        # "block_diag",
        # "bmm",
        # "broadcast_shapes",
        # "broadcast_tensors",
        # "broadcast_to",
        # "can_cast",
        # "cartesian_prod",
        "cat",
        "cdist",
        "ceil",
        # "chain_matmul",
        "cholesky",
        "chunk",
        "clamp",
        "clip",
        "clone",
        "column_stack",
        "complex",
        "concat",
        "conj",
        # "conj_physical",
        # "copysign",
        # "corrcoef",
        "cos",
        "cosh",
        # "count_nonzero",
        # "cov",
        "cross",
        # "cummax",
        # "cumprod",
        "cumsum",
        # "deg2rad",
        "det",
        "diag",
        # "diag_embed",
        "diagflat",
        "diagonal",
        # "diagonal_scatter",
        # "diff",
        # "dist",
        "div",
        "divide",
        "dot",
        "einsum",
        "empty",
        # "empty_like",
        # "empty_strided",
        "eq",
        "equal",
        "erf",
        "erfc",
        # "erfinv",
        "exp",
        "exp2",
        "expm1",
        "eye",
        "finfo",
        # "fix",
        "flatten",
        "flip",
        "floor",
        "floor_divide",
        "fmod",
        "frac",
        "full",
        "full_like",
        "gather",
        # "gcd",
        "ge",
        "ger",
        # "get_default_dtype",
        # "gradient",
        "greater",
        "greater_equal",
        "gt",
        "index_add",
        "index_copy",
        # "index_reduce",
        "index_select",
        "inverse",
        # "is_complex",
        # "is_floating_point",
        # "is_nonzero",
        # "is_tensor",
        "isclose",
        "isfinite",
        "isinf",
        "isnan",
        # "isneginf",
        # "isposinf",
        # "isreal",
        # "kaiser_window",
        # "kron",
        # "kthvalue",
        # "lcm",
        # "ldexp",
        "le",
        "lerp",
        "less",
        "less_equal",
        "lgamma",
        "linspace",
        "log",
        "log10",
        "log1p",
        "log2",
        "logaddexp",
        # "logaddexp2",
        "logcumsumexp",
        "logdet",
        # "logical_and",
        # "logical_not",
        # "logical_or",
        # "logical_xor",
        # "logit",
        # logspace,
        "logsumexp",
        # "lstm",
        "lt",
        # "lu_solve",
        # "manual_seed",
        "masked_fill",
        # "masked_select",
        "matmul",
        # "matrix_power",
        # "matrix_rank",
        "max",
        "maximum",
        "mean",
        "median",
        "meshgrid",
        "min",
        "minimum",
        "mm",
        # "moveaxis",
        # "movedim",
        # "msort",
        "mul",
        "multinomial",
        "multiply",
        "mv",
        # "mvlgamma",
        "nan_to_num",
        # "nanmean",
        # "nanmedian",
        # "nansum",
        "narrow",
        "ne",
        # "negative",
        # "nextafter",
        "nonzero",
        "norm",
        "normal",
        # "not_equal",
        "numel",
        "ones",
        "ones_like",
        "outer",
        "permute",
        "pinverse",
        # "poisson",
        # "polar",
        # "positive",
        "pow",
        "prod",
        "qr",
        # "quantile",
        # "rad2deg",
        "rand",
        "rand_like",
        "randint",
        "randint_like",
        "randn",
        "randn_like",
        "randperm",
        "range",
        # "ravel",
        # "real",
        "reciprocal",
        "relu",
        "remainder",
        # "renorm",
        # "repeat_interleave",
        "reshape",
        "result_type",
        "roll",
        "rot90",
        "round",
        "rsqrt",
        "scatter",
        "scatter_add",
        # "scatter_reduce",
        # "searchsorted",
        # "seed",
        "select",
        # "set_default_dtype",
        # "set_rng_state",
        # "sgn",
        "sigmoid",
        "sign",
        "sin",
        "sinh",
        # "slogdet",
        "softmax",
        "sort",
        "split",
        "sqrt",
        "square",
        "squeeze",
        "stack",
        "std",
        "std_mean",
        "sub",
        "subtract",
        "sum",
        # "svd",
        "swapaxes",
        # "swapdims",
        "t",
        # "take",
        # "take_along_dim",
        "tan",
        "tanh",
        "tensor",
        # "tensor_split",
        "tensordot",
        "tile",
        "topk",
        "transpose",
        "tril",
        "tril_indices",
        "triu",
        "triu_indices",
        "true_divide",
        "trunc",
        "unbind",
        "unflatten",
        "unique",
        "unique_consecutive",
        "unsqueeze",
        # "vander",
        "var",
        "var_mean",
        # "vdot",
        # "view_as_complex",
        # "view_as_real",
        # "vmap",
        # "vsplit",
        # "vstack",
        "where",
        # "xlogy",
        "zeros",
        "zeros_like",
    ],
    "torch.nn.functional": [
        "adaptive_avg_pool1d",
        "adaptive_avg_pool2d",
        "adaptive_max_pool2d",
        # "adaptive_max_pool3d",
        # "affine_grid",
        # "alpha_dropout",
        "avg_pool1d",
        "avg_pool2d",
        # "avg_pool3d",
        "batch_norm",
        "binary_cross_entropy",
        # "binary_cross_entropy_with_logits",
        "celu",
        # "celu_",
        "conv1d",
        "conv2d",
        "conv3d",
        "conv_transpose1d",
        "conv_transpose2d",
        # "conv_transpose3d",
        # "cosine_embedding_loss",
        # "cosine_similarity",
        "cross_entropy",
        "dropout",
        # "dropout1d",
        "dropout2d",
        "dropout3d",
        "elu",
        # "elu_",
        # "embedding",
        "fold",
        # "gaussian_nll_loss",
        "gelu",
        # "glu",
        # "grid_sample",
        "group_norm",
        "gumbel_softmax",
        "hardshrink",
        "hardsigmoid",
        "hardswish",
        "hardtanh",
        # "hardtanh_",
        "hinge_embedding_loss",
        "huber_loss",
        "instance_norm",
        "interpolate",
        "kl_div",
        "l1_loss",
        "layer_norm",
        "leaky_relu",
        # "leaky_relu_",
        "linear",
        # "local_response_norm",
        "logsigmoid",
        "log_softmax",
        # "lp_pool1d",
        # "lp_pool2d",
        # "margin_ranking_loss",
        # "max_pool1d",
        "max_pool2d",
        # "max_pool3d",
        # "mish",
        "mse_loss",
        # "multi_head_attention_forward",
        # "multilabel_margin_loss",
        # "multilabel_soft_margin_loss",
        # "nll_loss",
        "normalize",
        "one_hot",
        "pad",
        # "pairwise_distance",
        # "pdist",
        # "pixel_shuffle",
        # "pixel_unshuffle",
        # "poisson_nll_loss",
        # "prelu",
        "relu",
        "relu6",
        # "relu_",
        "rrelu",
        # "rrelu_",
        # "scaled_dot_product_attention",
        "selu",
        "sigmoid",
        "silu",
        "smooth_l1_loss",
        "soft_margin_loss",
        "softmax",
        # "softmin",
        "softplus",
        "softshrink",
        "softsign",
        "tanh",
        # "tanhshrink",
        # "threshold_",
        "triplet_margin_loss",
        "upsample",
        "upsample_bilinear",
        "upsample_nearest",
    ],
}

ALL_TORCH_LAYERS = {
    "torch.nn": [
        "AdaptiveAvgPool1d",
        "AdaptiveAvgPool2d",
        # "AdaptiveAvgPool3d",
        # "AdaptiveLogSoftmaxWithLoss",
        "AdaptiveMaxPool1d",
        "AdaptiveMaxPool2d",
        # "AdaptiveMaxPool3d",
        # "AlphaDropout",
        # "AvgPool1d",
        "AvgPool2d",
        "AvgPool3d",
        # "BCELoss",
        # "BCEWithLogitsLoss",
        # "BatchNorm1d",
        "BatchNorm2d",
        "BatchNorm3d",
        # "Bilinear",
        # "CELU",
        # "CTCLoss",
        # "ChannelShuffle",
        # "CircularPad1d",
        # "CircularPad2d",
        # "CircularPad3d",
        # "ConstantPad1d",
        # "ConstantPad2d",
        # "ConstantPad3d",
        # "Container",
        # "Conv1d",
        "Conv2d",
        # "Conv3d",
        # "ConvTranspose1d",
        "ConvTranspose2d",
        # "ConvTranspose3d",
        # "CosineEmbeddingLoss",
        # "CosineSimilarity",
        # "CrossEntropyLoss",
        # "CrossMapLRN2d",
        # "DataParallel",
        "Dropout",
        # "Dropout1d",
        "Dropout2d",
        # "Dropout3d",
        # "ELU",
        # "Embedding",
        # "EmbeddingBag",
        "Flatten",
        "Fold",
        # "FractionalMaxPool2d",
        # "FractionalMaxPool3d",
        "GELU",
        # "GLU",
        "GRU",
        # "GRUCell",
        # "GaussianNLLLoss",
        "GroupNorm",
        # "Hardshrink",
        "Hardsigmoid",
        "Hardswish",
        "Hardtanh",
        # "HingeEmbeddingLoss",
        # "HuberLoss",
        "Identity",
        # "InstanceNorm1d",
        "InstanceNorm2d",
        # "InstanceNorm3d",
        # "KLDivLoss",
        "L1Loss",
        # "LPPool1d",
        # "LPPool2d",
        # "LPPool3d",
        "LSTM",
        # "LSTMCell",
        "LayerNorm",
        # "LazyBatchNorm1d",
        # "LazyBatchNorm2d",
        # "LazyBatchNorm3d",
        # "LazyConv1d",
        # "LazyConv2d",
        # "LazyConv3d",
        # "LazyConvTranspose1d",
        # "LazyConvTranspose2d",
        # "LazyConvTranspose3d",
        # "LazyInstanceNorm1d",
        # "LazyInstanceNorm2d",
        # "LazyInstanceNorm3d",
        # "LazyLinear",
        "LeakyReLU",
        "Linear",
        # "LocalResponseNorm",
        # "LogSigmoid",
        # "LogSoftmax",
        # "MSELoss",
        # "MarginRankingLoss",
        # "MaxPool1d",
        "MaxPool2d",
        # "MaxPool3d",
        # "MaxUnpool1d",
        # "MaxUnpool2d",
        # "MaxUnpool3d",
        # "Mish",
        "ModuleDict",
        "ModuleList",
        # "MultiLabelMarginLoss",
        # "MultiLabelSoftMarginLoss",
        # "MultiMarginLoss",
        # "MultiheadAttention",
        # "NLLLoss",
        # "NLLLoss2d",
        "PReLU",
        # "PairwiseDistance",
        # "ParameterDict",
        # "ParameterList",
        # "PixelShuffle",
        # "PixelUnshuffle",
        # "PoissonNLLLoss",
        # "RMSNorm",
        "RNN",
        # "RNNBase",
        # "RNNCell",
        # "RNNCellBase",
        "RReLU",
        "ReLU",
        # "ReLU6",
        # "ReflectionPad1d",
        # "ReflectionPad2d",
        # "ReflectionPad3d",
        # "ReplicationPad1d",
        # "ReplicationPad2d",
        # "ReplicationPad3d",
        "SELU",
        "Sequential",
        "SiLU",
        "Sigmoid",
        # "SmoothL1Loss",
        # "SoftMarginLoss",
        "Softmax",
        # "Softmax2d",
        # "Softmin",
        # "Softplus",
        # "Softshrink",
        # "Softsign",
        # "Tanh",
        # "Tanhshrink",
        # "Threshold",
        # "Transformer",
        # "TransformerDecoder",
        # "TransformerDecoderLayer",
        # "TransformerEncoder",
        # "TransformerEncoderLayer",
        # "TripletMarginLoss",
        # "TripletMarginWithDistanceLoss",
        # "Unflatten",
        "Upsample",
        "UpsamplingBilinear2d",
        # "UpsamplingNearest2d",
        # "ZeroPad1d",
        "ZeroPad2d",
        # "ZeroPad3d",
    ]
}
