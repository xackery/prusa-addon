# prusa-addon
Prusa Slicer Blender Addon

This addon adds a new File, Export to blender called Prusa Slicer (.stl).

- If a mesh is hidden, it won't be exported.
- If a mesh has the name "Cutter", it won't be exported (boxcutter feature)


I often have cases like this, e.g. a modifier is being applied to a cube, or I have a giant cube just hidden for ref or some such. When you export to blender normally, this data ends up like: 
![image](https://github.com/xackery/prusa-addon/assets/845670/246c96dd-9629-46c0-a3a9-81146f88004e)

When this exports to prusa slicer via the File, Export, STL option, no matter what settings you use, it will make hidden objects visible:
![image](https://github.com/xackery/prusa-addon/assets/845670/2807441d-3783-4193-9863-19ff73bdb008)

When this addon is used, via File, Export, Prusa Slicer (.stl), the same file ends up like this:
![image](https://github.com/xackery/prusa-addon/assets/845670/ff18f782-2d4b-46fe-b144-b9530a632196)


