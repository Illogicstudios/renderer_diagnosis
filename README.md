# Renderer Diagnosis

> Renderer Diagnosis is a tool to analyse a scene and give informations about the amount of polygons of each asset

<div align="center">
  <br/>
  <span>
    <img src="https://github.com/Illogicstudios/renderer_diagnosis/assets/117286626/499b8eeb-7b94-42d5-bd25-f2031678b3c2" width=100%>
  </span>
  <p weight="bold">User interface of the Renderer Diagnosis</p>
  <br/>
</div>

## How to install

You will need some files that several Illogic tools need. You can get them via this link :
https://github.com/Illogicstudios/common

---

## Features

### Diagnosis

<div align="center">
  <span>
    <img src="https://github.com/Illogicstudios/renderer_diagnosis/assets/117286626/e4ffe3e2-b27e-4ac2-856e-58aa95b409c2" width=45%>
  </span>
  <br/>
  <br/>
</div>

To scan and analyse the scene you can click one of these buttons. If you want to diagnose only certain elements use the *Diagnose selection* button. The checkbox lets you choose whether you want the hidden objects or not.

---

In the following lists there are color indicators. they follow the color gradient at the bottom of the window :

<div align="center">
  <span>
    <img src="https://github.com/Illogicstudios/renderer_diagnosis/assets/117286626/b15384d6-bcdc-480a-86f3-8612c951a37d" width=100%>
  </span>
  <br/>
  <br/>
</div>

### Polygons of the hierarchy

<div align="center">
  <span>
    <img src="https://github.com/Illogicstudios/renderer_diagnosis/assets/117286626/f85baf37-5857-464b-bb0a-3a46aad8772a" width=55%>
  </span>
  <br/>
  <br/>
</div>

On the left there is a tree showing for each element in the scene the polygons count and the proportion of the scene that it takes (with a color indicator). Each sublist of elements is sorted to have the bigger first.

### Polygons of each asset

<div align="center">
  <span>
    <img src="https://github.com/Illogicstudios/renderer_diagnosis/assets/117286626/28f7f5d2-f4ca-412d-a57f-ff6556009b3c" width=70%>
  </span>
  <br/>
  <br/>
</div>

On the right there is a list of each topology in the scene sorted by their size. There are the polygons count, the proportion the topology takes (the color indicator shows the ratio with the biggest one) and the number of subdivisions.
