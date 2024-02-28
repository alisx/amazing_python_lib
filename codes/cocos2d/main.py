# pip install cocos2d

import cocos

class HelloWorld(cocos.layer.Layer):
    def __init__(self):
        super(HelloWorld, self).__init__()
        # 创建并添加一个标签到这个  layer
        label = cocos.text.Label('Hello, world',
                                 font_name='Times New Roman',
                                 font_size=32,
                                 anchor_x='center', anchor_y='center')
        label.position = 320, 240
        self.add(label)
        
        # 创建一个粒子系统 
        particle_system = cocos.particle_systems.Fireworks()
        # 将粒子系统添加到场景中 
        self.add(particle_system)

if __name__ == "__main__":
    # 初始化导演 
    cocos.director.director.init()
    # 创建一个  layer
    hello_layer = HelloWorld ()
    # 创建一个场景包含这个  layer
    main_scene = cocos.scene.Scene(hello_layer)
    # 运行场景 
    cocos.director.director.run(main_scene)
    
