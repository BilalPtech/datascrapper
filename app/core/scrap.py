import json
from app.utils.getSoup import get_soup
from app.utils.getHrefs import get_article_hrefs
from app.utils.getContent import extract_content_from_div

def get_blogs(base_url,dates):
    main_soup = get_soup(base_url)
    data = {}
    brand_div = main_soup.find('div',{'class':'site-branding-text'})
    brand_p = brand_div.find('p',{'class':'site-title'})
    data["site_url"] = brand_p.find('a')['href']
    data["site_title"] = brand_p.find('a').text
    data['site_description'] = brand_div.find('p',{'class':'site-description'}).text
    data["AllContent"] = []
    for date in dates:
        url = base_url+date
        blog_links = get_article_hrefs(url)
        for blog_link in blog_links:
            print(blog_link)
            blog={}
            article_soup = get_soup(blog_link)
            article_sec = article_soup.find('article')
            header = article_sec.find('header',{'class':'entry-header'})
            blog['Title'] = header.find('h1').text.strip()
            blog['postTimeDate'] = header.find('time').text.strip()
            art_div = article_sec.find('div',{'class':'entry-content'})
            ext_data = extract_content_from_div(art_div)
            blog['Text'] = ext_data['Text']
            blog['Media'] = ext_data['mediaLinks']
            data['AllContent'].append(blog)
    return data

def write_data_to_json(data, out_path):
    with open(out_path,'w') as f:
        json.dump(data, f, indent=4)