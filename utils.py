# because python doesn't have a builtin flatmap for some reason
def flatmap(func, iterables):
    return [item for iter in iterables for item in func(iter)]


target_scalars = [
    "cam_out_NETSW",
    "cam_out_FLWDS",
    "cam_out_PRECSC",
    "cam_out_PRECC",
    "cam_out_SOLS",
    "cam_out_SOLL",
    "cam_out_SOLSD",
    "cam_out_SOLLD",
]

target_vectors_base = [
    "ptend_t",
    "ptend_q0001",
    "ptend_q0002",
    "ptend_q0003",
    "ptend_u",
    "ptend_v",
]


def concat60(base):
    return [f"{base}_{i}" for i in range(60)]


# concat the 60 levels
target_vectors = flatmap(concat60, target_vectors_base)

target_cols = target_scalars + target_vectors


feat_scalars = [
    "state_ps",
    "pbuf_SOLIN",
    "pbuf_LHFLX",
    "pbuf_SHFLX",
    "pbuf_TAUX",
    "pbuf_TAUY",
    "pbuf_COSZRS",
    "cam_in_ALDIF",
    "cam_in_ALDIR",
    "cam_in_ASDIF",
    "cam_in_ASDIR",
    "cam_in_LWUP",
    "cam_in_ICEFRAC",
    "cam_in_LANDFRAC",
    "cam_in_OCNFRAC",
    "cam_in_SNOWHLAND",
]


feat_vectors_base = [
    "state_t",
    "state_q0001",
    "state_q0002",
    "state_q0003",
    "state_u",
    "state_v",
    "pbuf_ozone",
    "pbuf_CH4",
    "pbuf_N2O",
]

feat_vectors = flatmap(concat60, feat_vectors_base)

feat_cols = feat_scalars + feat_vectors
