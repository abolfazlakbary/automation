read domain

    # Create directory based on the input domain
    mkdir "$domain"

    # Process URLs and save to files
    echo "$domain" | waybackurls | grep -Eiv '.(css|jpg|jpeg|png|svg|img|gif|exe|mp4|flv|pdf|doc|ogv|webm|wmv|webp|mov|mp3|m4a|m4p|ppt|pptx|scss|tif|tiff|ttf|otf|woff|woff2|bmp|ico|eot|htc|swf|rtf|image|rf)' | sort -u | tee "$domain/waybackurls.txt"
    echo "$domain" | gau | grep -Eiv '.(css|jpg|jpeg|png|svg|img|gif|exe|mp4|flv|pdf|doc|ogv|webm|wmv|webp|mov|mp3|m4a|m4p|ppt|pptx|scss|tif|tiff|ttf|otf|woff|woff2|bmp|ico|eot|htc|swf|rtf|image|rf)' | sort -u | tee "$domain/gau.txt"
    echo "$domain" | katana -js-crawl -known-files -automatic-form-fill -silent -crawl-scope "$domain" -extension-filter css,jpg,jpeg,png,svg,img,gif,mp4,flv,pdf,doc,ogv,webm,wmv,webp,mov,mp3,m4a,m4p,ppt,pptx,scss,tif,tiff,ttf,otf,woff,woff2,bmp,ico,eot,htc,swf,rtf,image -headers 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:108.0) Gecko/20100101 Firefox/108.0' | tee "$domain/katana.txt"

    # Combine results and run httpx
    cat "$domain/waybackurls.txt" "$domain/gau.txt" "$domain/katana.txt" | sort -u | httpx >> "$domain/crawl.txt"