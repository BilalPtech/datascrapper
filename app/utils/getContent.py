def extract_content_from_div(parent_div):
    writing = []
    links = []
    extracted_data = {}

    for child in parent_div.children:
        tag_name = child.name

        if tag_name == 'p':
            print('<p>')
            text = child.get_text(strip=True)
            if text:
                writing.append(text)
            images = child.find_all('img')
            if images:
                for img in images:
                    img_src = img.get('src')
                    if img_src:
                        links.append(img_src)
        elif tag_name == 'div' and child.get('id') != "jp-post-flair":
            print('<div>')
            images = child.find_all('img')
            for img in images:
                img_src = img.get('src')
                if img_src:
                    links.append(img_src)
        elif tag_name == 'figure':
            print('<figure>')
            images = child.find_all('img')
            for img in images:
                img_src = img.get('src')
                if img_src:
                    links.append(img_src)

            iframes = child.find_all('iframe')
            for iframe in iframes:
                iframe_src = iframe.get('src')
                if iframe_src:
                    links.append(iframe_src)

        elif tag_name in ['ol', 'ul']:
            print('<ol|ul>')
            list_items = child.find_all('li')
            for item in list_items:
                item_text = item.get_text(strip=True)
                if item_text:
                    writing.append(item_text)

    extracted_data['Text'] = writing
    extracted_data['mediaLinks'] = links
    
    return extracted_data