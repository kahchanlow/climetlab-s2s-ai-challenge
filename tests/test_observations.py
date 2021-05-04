import os

import climetlab as cml

if os.environ.get("TEST_FAST"):
    is_test = "-dev"  # short tests
else:
    is_test = ""  # long tests


def test_get_obs():

    cmlds = cml.load_dataset(
        "s2s-ai-challenge-observations",
        date=20200312,
        parameter="2t",
    )
    ds = cmlds.to_xarray()
    print(ds)