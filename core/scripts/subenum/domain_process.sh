read domain

    mkdir "$domain"

    echo "$domain" | waybackurls | grep -Eiv '.(css|jpg|jpeg|png|svg|img|gif|ex$
    echo "$domain" | gau | grep -Eiv '.(css|jpg|jpeg|png|svg|img|gif|exe|mp4|fl$
    echo "$domain" | katana -js-crawl -known-files -automatic-form-fill -silent$

    cat "$domain/waybackurls.txt" "$domain/gau.txt" "$domain/katana.txt" | sort$