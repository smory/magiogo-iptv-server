import re

MAX_RESOLUTION = 1080

mpd = u"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<!--Created with VSPP Streamer version 8.0.5.0 build  Commit_id: 91b1e7409ceac6d82616508e4f9dabda60b8d4d3 Commit_time: 1693228913 context 3664748125981805004-MAAAAAAACAKJHLFG-->
<MPD
	xmlns="urn:mpeg:dash:schema:mpd:2011"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" profiles="urn:mpeg:dash:profile:isoff-live:2011" type="dynamic" availabilityStartTime="1970-01-01T00:00:00Z" publishTime="2024-02-07T14:57:20Z" timeShiftBufferDepth="PT1M0S" minimumUpdatePeriod="PT4S" maxSegmentDuration="PT4.011S" minBufferTime="PT12S">
	<Period id="1" start="PT0S">
		<AdaptationSet id="1" group="1" bitstreamSwitching="true" segmentAlignment="true" contentType="video" mimeType="video/mp4" maxWidth="1920" maxHeight="1080" par="16:9" maxFrameRate="50" startWithSAP="1">
			<SegmentTemplate timescale="10000000" media="https://vlive05.cdn.magio.tv/sdash/LIVE$PLUS_HD_OTT/index.mpd/___SIGN_CIP88.212.40.129_ET1707403770_US258380768b10cfcf598cd8346912feb86c698b48___/S!d2EaT1RUX0JJR1NDUkVFTl9EQVNIXzRfNEtfdjISBFT-....ARYInw__/QualityLevels($Bandwidth$,Level_params=$RepresentationID$)/Fragments(video=$Time$)" initialization="https://vlive05.cdn.magio.tv/sdash/LIVE$PLUS_HD_OTT/index.mpd/___SIGN_CIP88.212.40.129_ET1707403770_US258380768b10cfcf598cd8346912feb86c698b48___/S!d2EaT1RUX0JJR1NDUkVFTl9EQVNIXzRfNEtfdjISBFT-....ARYInw__/QualityLevels($Bandwidth$,Level_params=$RepresentationID$)/Fragments(video=Init)">
				<SegmentTimeline>
					<S t="17073177679379360" d="40000000" r="14"/>
				</SegmentTimeline>
			</SegmentTemplate>
			<Representation id="dxADMUB-BRIbnw.." bandwidth="360000" codecs="avc1.640015" width="480" height="270" frameRate="25" sar="1:1" scanType="progressive"/>
			<Representation id="dxADMSDWExIbnw.." bandwidth="1300000" codecs="avc1.64001f" width="960" height="540" frameRate="25" sar="1:1" scanType="progressive"/>
			<Representation id="dxADMQCfJBIbnw.." bandwidth="2400000" codecs="avc1.64001f" width="1280" height="720" frameRate="25" sar="1:1" scanType="progressive"/>
			<Representation id="dxADMUDhMxIbnw.." bandwidth="3400000" codecs="avc1.64001f" width="1280" height="720" frameRate="25" sar="1:1" scanType="progressive"/>
			<Representation id="dxADMUBLTBIbnw.." bandwidth="5000000" codecs="avc1.64002a" width="1920" height="1080" frameRate="50" sar="1:1" scanType="progressive"/>
		</AdaptationSet>
		<AdaptationSet id="2" group="2" bitstreamSwitching="true" segmentAlignment="true" contentType="audio" mimeType="audio/mp4" lang="slk">
			<AudioChannelConfiguration schemeIdUri="urn:mpeg:dash:23003:3:audio_channel_configuration:2011" value="2"/>
			<SegmentTemplate timescale="48000" media="https://vlive05.cdn.magio.tv/sdash/LIVE$PLUS_HD_OTT/index.mpd/___SIGN_CIP88.212.40.129_ET1707403770_US258380768b10cfcf598cd8346912feb86c698b48___/S!d2EaT1RUX0JJR1NDUkVFTl9EQVNIXzRfNEtfdjISBFT-....ARYInw__/QualityLevels($Bandwidth$,Level_params=$RepresentationID$)/Fragments(audio_482_slk=$Time$)" initialization="https://vlive05.cdn.magio.tv/sdash/LIVE$PLUS_HD_OTT/index.mpd/___SIGN_CIP88.212.40.129_ET1707403770_US258380768b10cfcf598cd8346912feb86c698b48___/S!d2EaT1RUX0JJR1NDUkVFTl9EQVNIXzRfNEtfdjISBFT-....ARYInw__/QualityLevels($Bandwidth$,Level_params=$RepresentationID$)/Fragments(audio_482_slk=Init)">
				<SegmentTimeline>
					<S t="81951252861980" d="191488"/>
					<S d="192512"/>
					<S d="191488"/>
					<S d="192512"/>
					<S d="191488"/>
					<S d="192512"/>
					<S d="191488"/>
					<S d="192512"/>
					<S d="191488"/>
					<S d="192512"/>
					<S d="191488"/>
					<S d="192512"/>
					<S d="191488"/>
					<S d="192512"/>
					<S d="191488"/>
				</SegmentTimeline>
			</SegmentTemplate>
			<Representation id="dxADIeIBnw.." bandwidth="128000" codecs="mp4a.40.2" audioSamplingRate="48000"/>
		</AdaptationSet>
		<AdaptationSet id="3" group="2" bitstreamSwitching="true" segmentAlignment="true" contentType="audio" mimeType="audio/mp4" lang="mul">
			<AudioChannelConfiguration schemeIdUri="urn:mpeg:dash:23003:3:audio_channel_configuration:2011" value="2"/>
			<SegmentTemplate timescale="48000" media="https://vlive05.cdn.magio.tv/sdash/LIVE$PLUS_HD_OTT/index.mpd/___SIGN_CIP88.212.40.129_ET1707403770_US258380768b10cfcf598cd8346912feb86c698b48___/S!d2EaT1RUX0JJR1NDUkVFTl9EQVNIXzRfNEtfdjISBFT-....ARYInw__/QualityLevels($Bandwidth$,Level_params=$RepresentationID$)/Fragments(audio_483_mul=$Time$)" initialization="https://vlive05.cdn.magio.tv/sdash/LIVE$PLUS_HD_OTT/index.mpd/___SIGN_CIP88.212.40.129_ET1707403770_US258380768b10cfcf598cd8346912feb86c698b48___/S!d2EaT1RUX0JJR1NDUkVFTl9EQVNIXzRfNEtfdjISBFT-....ARYInw__/QualityLevels($Bandwidth$,Level_params=$RepresentationID$)/Fragments(audio_483_mul=Init)">
				<SegmentTimeline>
					<S t="81951252861980" d="191488"/>
					<S d="192512"/>
					<S d="191488"/>
					<S d="192512"/>
					<S d="191488"/>
					<S d="192512"/>
					<S d="191488"/>
					<S d="192512"/>
					<S d="191488"/>
					<S d="192512"/>
					<S d="191488"/>
					<S d="192512"/>
					<S d="191488"/>
					<S d="192512"/>
					<S d="191488"/>
				</SegmentTimeline>
			</SegmentTemplate>
			<Representation id="dxADIeMBnw.." bandwidth="128000" codecs="mp4a.40.2" audioSamplingRate="48000"/>
		</AdaptationSet>
		<AdaptationSet id="4" group="8" bitstreamSwitching="true" segmentAlignment="true" contentType="text" mimeType="application/mp4" lang="slo">
			<Role schemeIdUri="urn:mpeg:dash:role:2011" value="subtitle"/>
			<SegmentTemplate timescale="10000000" media="https://vlive05.cdn.magio.tv/sdash/LIVE$PLUS_HD_OTT/index.mpd/___SIGN_CIP88.212.40.129_ET1707403770_US258380768b10cfcf598cd8346912feb86c698b48___/S!d2EaT1RUX0JJR1NDUkVFTl9EQVNIXzRfNEtfdjISBFT-....ARYInw__/QualityLevels($Bandwidth$,Level_params=$RepresentationID$)/Fragments(slo_0=$Time$)" initialization="https://vlive05.cdn.magio.tv/sdash/LIVE$PLUS_HD_OTT/index.mpd/___SIGN_CIP88.212.40.129_ET1707403770_US258380768b10cfcf598cd8346912feb86c698b48___/S!d2EaT1RUX0JJR1NDUkVFTl9EQVNIXzRfNEtfdjISBFT-....ARYInw__/QualityLevels($Bandwidth$,Level_params=$RepresentationID$)/Fragments(slo_0=Init)">
				<SegmentTimeline>
					<S t="17073177679379360" d="40000000" r="14"/>
				</SegmentTimeline>
			</SegmentTemplate>
			<Representation id="dxADEWSf" bandwidth="100" codecs="stpp"/>
		</AdaptationSet>
	</Period>
</MPD>"""

mpd2 = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<!--Created with VSPP Streamer version 8.0.5.0 build  Commit_id: 91b1e7409ceac6d82616508e4f9dabda60b8d4d3 Commit_time: 1693228913 context 3664766459049874355-DOGBAAAALFLLHLFG-->
<MPD xmlns="urn:mpeg:dash:schema:mpd:2011" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" profiles="urn:mpeg:dash:profile:isoff-live:2011" type="dynamic" availabilityStartTime="1970-01-01T00:00:00Z" publishTime="2024-02-08T09:39:58Z" timeShiftBufferDepth="PT1M0S" minimumUpdatePeriod="PT4S" maxSegmentDuration="PT4.011S" minBufferTime="PT12S"><BaseURL>https://vlive06.cdn.magio.tv/sdash/LIVE$Jednotka_HD_OTT/index.mpd/___SIGN_CIP88.212.40.129_ET1707471601_UScdc7c327f3276cfd1b8808da14c6a19e4435f3bc___/</BaseURL><Period id="1" start="PT0S"><AdaptationSet id="1" group="1" bitstreamSwitching="true" segmentAlignment="true" contentType="video" mimeType="video/mp4" maxWidth="1920" maxHeight="1080" par="16:9" maxFrameRate="50" startWithSAP="1"><SegmentTemplate timescale="10000000" media="S!d2EaT1RUX0JJR1NDUkVFTl9EQVNIXzRfNEtfdjISBFT-....ARYInw__/QualityLevels($Bandwidth$,Level_params=$RepresentationID$)/Fragments(video=$Time$)" initialization="S!d2EaT1RUX0JJR1NDUkVFTl9EQVNIXzRfNEtfdjISBFT-....ARYInw__/QualityLevels($Bandwidth$,Level_params=$RepresentationID$)/Fragments(video=Init)"><SegmentTimeline><S t="17073851258282210" d="40000000" r="14"/></SegmentTimeline></SegmentTemplate><Representation id="dxADMUB-BRIbnw.." bandwidth="360000" codecs="avc1.640015" width="480" height="270" frameRate="25" sar="1:1" scanType="progressive"/><Representation id="dxADMSDWExIbnw.." bandwidth="1300000" codecs="avc1.64001f" width="960" height="540" frameRate="25" sar="1:1" scanType="progressive"/><Representation id="dxADMQCfJBIbnw.." bandwidth="2400000" codecs="avc1.64001f" width="1280" height="720" frameRate="25" sar="1:1" scanType="progressive"/><Representation id="dxADMUDhMxIbnw.." bandwidth="3400000" codecs="avc1.64001f" width="1280" height="720" frameRate="25" sar="1:1" scanType="progressive"/><Representation id="dxADMUBLTBIbnw.." bandwidth="5000000" codecs="avc1.64002a" width="1920" height="1080" frameRate="50" sar="1:1" scanType="progressive"/></AdaptationSet><AdaptationSet id="2" group="2" bitstreamSwitching="true" segmentAlignment="true" contentType="audio" mimeType="audio/mp4" lang="slo"><AudioChannelConfiguration schemeIdUri="urn:mpeg:dash:23003:3:audio_channel_configuration:2011" value="2"/><SegmentTemplate timescale="48000" media="S!d2EaT1RUX0JJR1NDUkVFTl9EQVNIXzRfNEtfdjISBFT-....ARYInw__/QualityLevels($Bandwidth$,Level_params=$RepresentationID$)/Fragments(audio_482_slo=$Time$)" initialization="S!d2EaT1RUX0JJR1NDUkVFTl9EQVNIXzRfNEtfdjISBFT-....ARYInw__/QualityLevels($Bandwidth$,Level_params=$RepresentationID$)/Fragments(audio_482_slo=Init)"><SegmentTimeline><S t="81954486040202" d="192512"/><S d="191488"/><S d="192512"/><S d="191488"/><S d="192512"/><S d="191488"/><S d="192512"/><S d="191488"/><S d="192512"/><S d="191488"/><S d="192512"/><S d="191488"/><S d="192512"/><S d="191488"/><S d="192512"/></SegmentTimeline></SegmentTemplate><Representation id="dxADIeIBnw.." bandwidth="128000" codecs="mp4a.40.2" audioSamplingRate="48000"/></AdaptationSet><AdaptationSet id="3" group="2" bitstreamSwitching="true" segmentAlignment="true" contentType="audio" mimeType="audio/mp4" lang="ads"><AudioChannelConfiguration schemeIdUri="urn:mpeg:dash:23003:3:audio_channel_configuration:2011" value="2"/><SegmentTemplate timescale="48000" media="S!d2EaT1RUX0JJR1NDUkVFTl9EQVNIXzRfNEtfdjISBFT-....ARYInw__/QualityLevels($Bandwidth$,Level_params=$RepresentationID$)/Fragments(audio_483_ads=$Time$)" initialization="S!d2EaT1RUX0JJR1NDUkVFTl9EQVNIXzRfNEtfdjISBFT-....ARYInw__/QualityLevels($Bandwidth$,Level_params=$RepresentationID$)/Fragments(audio_483_ads=Init)"><SegmentTimeline><S t="81954486040202" d="192512"/><S d="191488"/><S d="192512"/><S d="191488"/><S d="192512"/><S d="191488"/><S d="192512"/><S d="191488"/><S d="192512"/><S d="191488"/><S d="192512"/><S d="191488"/><S d="192512"/><S d="191488"/><S d="192512"/></SegmentTimeline></SegmentTemplate><Representation id="dxADIeMBnw.." bandwidth="128000" codecs="mp4a.40.2" audioSamplingRate="48000"/></AdaptationSet><AdaptationSet id="4" group="8" bitstreamSwitching="true" segmentAlignment="true" contentType="text" mimeType="application/mp4" lang="slo"><Role schemeIdUri="urn:mpeg:dash:role:2011" value="subtitle"/><SegmentTemplate timescale="10000000" media="S!d2EaT1RUX0JJR1NDUkVFTl9EQVNIXzRfNEtfdjISBFT-....ARYInw__/QualityLevels($Bandwidth$,Level_params=$RepresentationID$)/Fragments(slo_0=$Time$)" initialization="S!d2EaT1RUX0JJR1NDUkVFTl9EQVNIXzRfNEtfdjISBFT-....ARYInw__/QualityLevels($Bandwidth$,Level_params=$RepresentationID$)/Fragments(slo_0=Init)"><SegmentTimeline><S t="17073851258282210" d="40000000" r="14"/></SegmentTimeline></SegmentTemplate><Representation id="dxADEWSf" bandwidth="100" codecs="stpp"/></AdaptationSet></Period></MPD"""

mpd3 = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<!--Created with VSPP Streamer version 8.0.5.0 build  Commit_id: 91b1e7409ceac6d82616508e4f9dabda60b8d4d3 Commit_time: 1693228913 context 3663425507975761718-IFAAAAAAOCEDOKFG-->
<MPD xmlns="urn:mpeg:dash:schema:mpd:2011" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" profiles="urn:mpeg:dash:profile:isoff-live:2011" type="dynamic" availabilityStartTime="1970-01-01T00:00:00Z" publishTime="2024-02-08T09:46:46Z" timeShiftBufferDepth="PT1M0S" minimumUpdatePeriod="PT4S" maxSegmentDuration="PT4.011S" minBufferTime="PT12S"><BaseURL>https://vlive20.cdn.magio.tv/sdash/LIVE$JOJ_HD_OTT/index.mpd/___SIGN_CIP88.212.40.129_ET1707472009_US10080fd8c0d00d32d2c1e2ece7102a96a0028f5f___/</BaseURL><Period id="1" start="PT0S"><AdaptationSet id="1" group="1" bitstreamSwitching="true" segmentAlignment="true" contentType="video" mimeType="video/mp4" maxWidth="1920" maxHeight="1080" par="16:9" maxFrameRate="50" startWithSAP="1"><SegmentTemplate timescale="10000000" media="S!d2EaT1RUX0JJR1NDUkVFTl9EQVNIXzRfNEtfdjISBFT-....ARYInw__/QualityLevels($Bandwidth$,Level_params=$RepresentationID$)/Fragments(video=$Time$)" initialization="S!d2EaT1RUX0JJR1NDUkVFTl9EQVNIXzRfNEtfdjISBFT-....ARYInw__/QualityLevels($Bandwidth$,Level_params=$RepresentationID$)/Fragments(video=Init)"><SegmentTimeline><S t="17073855335590510" d="40000000" r="14"/></SegmentTimeline></SegmentTemplate><Representation id="dxADMUB-BRIbnw.." bandwidth="360000" codecs="avc1.640015" width="480" height="270" frameRate="25" sar="1:1" scanType="progressive"/><Representation id="dxADMSDWExIbnw.." bandwidth="1300000" codecs="avc1.64001f" width="960" height="540" frameRate="25" sar="1:1" scanType="progressive"/><Representation id="dxADMQCfJBIbnw.." bandwidth="2400000" codecs="avc1.64001f" width="1280" height="720" frameRate="25" sar="1:1" scanType="progressive"/><Representation id="dxADMUDhMxIbnw.." bandwidth="3400000" codecs="avc1.64001f" width="1280" height="720" frameRate="25" sar="1:1" scanType="progressive"/><Representation id="dxADMUBLTBIbnw.." bandwidth="5000000" codecs="avc1.64002a" width="1920" height="1080" frameRate="50" sar="1:1" scanType="progressive"/></AdaptationSet><AdaptationSet id="2" group="2" bitstreamSwitching="true" segmentAlignment="true" contentType="audio" mimeType="audio/mp4" lang="slk"><AudioChannelConfiguration schemeIdUri="urn:mpeg:dash:23003:3:audio_channel_configuration:2011" value="2"/><SegmentTemplate timescale="48000" media="S!d2EaT1RUX0JJR1NDUkVFTl9EQVNIXzRfNEtfdjISBFT-....ARYInw__/QualityLevels($Bandwidth$,Level_params=$RepresentationID$)/Fragments(audio_482_slk=$Time$)" initialization="S!d2EaT1RUX0JJR1NDUkVFTl9EQVNIXzRfNEtfdjISBFT-....ARYInw__/QualityLevels($Bandwidth$,Level_params=$RepresentationID$)/Fragments(audio_482_slk=Init)"><SegmentTimeline><S t="81954505611794" d="191488"/><S d="192512"/><S d="191488"/><S d="192512"/><S d="191488"/><S d="192512"/><S d="191488"/><S d="192512"/><S d="191488"/><S d="192512"/><S d="191488"/><S d="192512"/><S d="191488"/><S d="192512"/><S d="191488"/></SegmentTimeline></SegmentTemplate><Representation id="dxADIeIBnw.." bandwidth="128000" codecs="mp4a.40.2" audioSamplingRate="48000"/></AdaptationSet><AdaptationSet id="3" group="2" bitstreamSwitching="true" segmentAlignment="true" contentType="audio" mimeType="audio/mp4" lang="mul"><AudioChannelConfiguration schemeIdUri="urn:mpeg:dash:23003:3:audio_channel_configuration:2011" value="2"/><SegmentTemplate timescale="48000" media="S!d2EaT1RUX0JJR1NDUkVFTl9EQVNIXzRfNEtfdjISBFT-....ARYInw__/QualityLevels($Bandwidth$,Level_params=$RepresentationID$)/Fragments(audio_483_mul=$Time$)" initialization="S!d2EaT1RUX0JJR1NDUkVFTl9EQVNIXzRfNEtfdjISBFT-....ARYInw__/QualityLevels($Bandwidth$,Level_params=$RepresentationID$)/Fragments(audio_483_mul=Init)"><SegmentTimeline><S t="81954505611794" d="191488"/><S d="192512"/><S d="191488"/><S d="192512"/><S d="191488"/><S d="192512"/><S d="191488"/><S d="192512"/><S d="191488"/><S d="192512"/><S d="191488"/><S d="192512"/><S d="191488"/><S d="192512"/><S d="191488"/></SegmentTimeline></SegmentTemplate><Representation id="dxADIeMBnw.." bandwidth="128000" codecs="mp4a.40.2" audioSamplingRate="48000"/></AdaptationSet><AdaptationSet id="4" group="8" bitstreamSwitching="true" segmentAlignment="true" contentType="text" mimeType="application/mp4" lang="slo"><Role schemeIdUri="urn:mpeg:dash:role:2011" value="subtitle"/><SegmentTemplate timescale="10000000" media="S!d2EaT1RUX0JJR1NDUkVFTl9EQVNIXzRfNEtfdjISBFT-....ARYInw__/QualityLevels($Bandwidth$,Level_params=$RepresentationID$)/Fragments(slo_0=$Time$)" initialization="S!d2EaT1RUX0JJR1NDUkVFTl9EQVNIXzRfNEtfdjISBFT-....ARYInw__/QualityLevels($Bandwidth$,Level_params=$RepresentationID$)/Fragments(slo_0=Init)"><SegmentTimeline><S t="17073855335590510" d="40000000" r="14"/></SegmentTimeline></SegmentTemplate><Representation id="dxADEWSf" bandwidth="100" codecs="stpp"/></AdaptationSet></Period></MPD>
"""

url = u' https://vpvr06.cdn.magio.tv/sdash/ott-movie-630867212/index.mpd/___SIGN_CIP88.212.40.129_ET1707358288_USec4cf3335249106a2fcb47f4f4a8f2e3deb2ed87___/Manifest?device=OTT_BIGSCREEN_DASH_4_4K'


def insert_base_url(manifest: str, url: str):
    root_match = re.search("<MPD.*?>", manifest, re.DOTALL | re.MULTILINE)
    if (root_match):
        base_url = "<BaseURL>" + url + "</BaseURL>"
        return manifest[:root_match.end()] + base_url + manifest[root_match.end():]
    return manifest


def modify_video_tracks(manifest: str):
    matches = re.finditer("<Representation.*?height=\"(\d*).*?/>", manifest)
    best_height = 0
    best_element = None
    list_to_remove = []
    for m in matches:
        height = int(m.groups()[0])
        element = m.group()
        if best_height <= height <= MAX_RESOLUTION:
            if best_element:
                list_to_remove.append(best_element)
            best_height = height
            best_element = element
        else:
            list_to_remove.append(element)

    m = manifest
    for s in list_to_remove:
        m = m.replace(s, '', 1)

    return m


def modify_manifest(manifest: str, manifest_url: str):
    base_url = get_base_url(manifest_url)
    m = insert_base_url(manifest, base_url)
    m = modify_video_tracks(m)
    return m


def get_base_url(manifest_url: str):
    return manifest_url.split("Manifest")[0]


if __name__ == '__main__':
    # modify_manifest(mpd, url)
    modify_video_tracks(mpd)
