import re

MAX_RESOLUTION = 1080


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


def modify_manifest(manifest: str, manifest_url: str, remove_smaller_resolutions: bool):
    base_url = get_base_url(manifest_url)
    m = insert_base_url(manifest, base_url)
    if remove_smaller_resolutions:
        m = modify_video_tracks(m)
    return m


def get_base_url(manifest_url: str):
    return manifest_url.split("Manifest")[0]


if __name__ == '__main__':
    pass
