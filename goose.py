from goose import Goose
url='http://www.amazon.in/Apple-iPhone-6S-Rose-Gold/dp/B01LXF3SP9/ref=gbph_img_m-8_46d0_76c5f271?smid=A21HMA0I25QPU0&pf_rd_p=da6e031c-a3e5-416b-96d7-4de2bb5346d0&pf_rd_s=merchandised-search-8&pf_rd_t=101&pf_rd_i=1389401031&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_r=11WJ2D57XE2PHG3593S7'
g=Goose()
article=g.extract(url=url)
article.title
# article.meta_description
# article.cleaned_text[:150]
# article.top_image.src