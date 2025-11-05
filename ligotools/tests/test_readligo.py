from ligotools import readligo as rl
import json
from pathlib import Path

def test_loaddata():
    root = Path(__file__).resolve().parents[2]
    fnjson = root / "data" / "BBH_events_v3.json"
    with open(fnjson, "r") as f:
        events = json.load(f)
    eventname = 'GW150914'
    event = events[eventname]
    fn_H1 = root / "data" / event["fn_H1"]
    strain_H1, time_H1, chan_dict_H1 = rl.loaddata(str(fn_H1), "H1")

    assert len(strain_H1) == len(time_H1)
    assert isinstance(chan_dict_H1, dict)

def test_dq_channel_to_seglist():
    root = Path(__file__).resolve().parents[2]
    fnjson = root / "data" / "BBH_events_v3.json"
    with open(fnjson, "r") as f:
        events = json.load(f)
    eventname = 'GW150914'
    event = events[eventname]
    fn_L1 = root / "data" / event["fn_L1"]

    strain, time, chan_dict = rl.loaddata(fn_L1, 'H1')
    segment_lst = rl.dq_channel_to_seglist(chan_dict['BURST_CAT3'])
    for segment in segment_lst:
	    time_seg = time[segment]
	    seg_strain = strain[segment]
	    assert len(seg_strain) == 131072
	    assert time_seg[0] == 1126259446.0
	    assert time_seg[-1] == 1126259477.9997559