screen new_screen:
  side "c r":
    area(0, 0, 1280, 1000)

    viewport id "vp":
      area(160, 0, 1280, 720)
      draggable True
      mousewheel True

      vbox:
      
        python:
          items = []
          items.append(["smpletan", "beenleship.png", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."])
          items.append(["smpletong", "beenleship.png", "nice lorem ipsum spam, jackass"])
          items.append(["smpletong", "beenleship.png", "nice lorem ipsum spam, jackass"])


        for i in items:
          frame:
            maximum (960, 300)
            padding (0, 0)
            xalign 0.05
            yalign 0.5
  
            hbox:
                vbox:
                    minimum(200, 300)
                    frame:
                      align(0.5, 0.2)
                      margin (10, 10)
                      minimum (100, 50)
                      text "[i[0]]" align (0.5, 0.5)
  
                    add "[i[1]]" xalign 0.5
  
                hbox:
                  frame:
                    padding (50, 50)
                    minimum (760, 300)
                    text "[i[2]]" minimum (700, 250) min_width 700

    vbar value YScrollValue("vp")  