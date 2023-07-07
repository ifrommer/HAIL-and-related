### Roboflow cheat sheet
- if you upload a video, it will split it into still images, prompting you for a frame rate
- See the capstone guide to using roboflow
- From video https://youtu.be/pJaM06FG-wQ  (very helpful)
    - create as specific labels as possible for the context (e.g. i_benz, i_altima) b/c can always combine them later if desired (e.g. i_car, or car)
    - use tight bounding boxes as tight as possible without cutting off any of the object
    - label all objects of interest (in his ex., he labels every pawn piece)
    - label occluded (blocked) objects and it's ok (in fact encouraged) if the bounding box includes part of what is blocking the object
    - write clear labeling instructions and share them with your team
