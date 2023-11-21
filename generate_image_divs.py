generator_string = """
                        <div class="col-md-4 col-sm-6">
                            <div class="item">
                                <div class="thumb">
                                    <a href="img/gallery/{0}_bg.jpg" data-lightbox="image-1">
                                        <div class="hover-effect">
                                        </div>
                                    </a>
                                    <div class="image">
                                        <img src="img/gallery/{0}.jpg">
                                    </div>
                                </div>
                            </div>
                        </div>
"""

with open("generated_divs", "w") as file1:
    for i in range(1, 62):
        file1.write(generator_string.format(i))
