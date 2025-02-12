from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QColorDialog,
    QMessageBox,
    QWidget,
    QLabel,
    QVBoxLayout,
    QToolBar,
    QLabel,
)
from PyQt6.QtGui import QColor, QIcon
from PyQt6.QtCore import Qt, QPointF
import sys
from default_theme import DeafultTheme
import app_themes.colors as colors


class CalmIris_win(QMainWindow):
    def __init__(self):
        super().__init__()
        self.widget = QWidget()
        self.setCentralWidget(self.widget)
        self.setWindowIcon(QIcon("C:/Users/1973r/OneDrive/Desktop/PyQt_apps/CalmIris/app_icon/calmiris_icon.png"))
        self.setWindowTitle("CalmIris")
        self.setGeometry(100, 100, 1000, 550)
        self.setFixedSize(1000, 550)

        self.default_theme = DeafultTheme.default_theme()

        if self.default_theme:
            self.setStyleSheet(self.default_theme)
        else:
            self.setStyleSheet(DeafultTheme.default_theme())

        toolbar = QToolBar()
        self.addToolBar(toolbar)
        toolbar.setMovable(False)

        self.label = QLabel()
        self.label.setText("CalmIris")
        self.label.setObjectName("label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # self.label.setStyleSheet(DeafultTheme.default_theme())

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.widget.setLayout(self.layout)

        # Sky blue color
        self.sky_blue_btn = toolbar.addAction("Sky Blue")
        self.sky_blue_btn.setIcon(QIcon(
            "C:/Users/1973r/OneDrive/Desktop/PyQt_apps/CalmIris/toolbar_icons/sky_blue.png"))
        self.sky_blue_btn.setObjectName("sky_blue")

        self.sky_blue_btn.triggered.connect(self.apply_sky_blue_theme)

        # Shaded green color
        self.mint_green__btn = toolbar.addAction("Shaded Green")
        self.mint_green__btn.setIcon(QIcon(
            'C:/Users/1973r/OneDrive/Desktop/PyQt_apps/CalmIris/toolbar_icons/mint_green_btn.png'))
        self.mint_green__btn.setToolTip('Shaded green')
        self.mint_green__btn.setObjectName('Shaded green')
        self.mint_green__btn.triggered.connect(self.apply_mint_green_btn)

        # muted shade of teal
        self.muted_teal_btn = toolbar.addAction('Muted Teal')
        self.muted_teal_btn.setIcon(QIcon(
            'C:/Users/1973r/OneDrive/Desktop/PyQt_apps/CalmIris/toolbar_icons/muted_shade_of_teal.png'))
        self.muted_teal_btn.setToolTip('Muted Teal')
        self.muted_teal_btn.triggered.connect(self.apply_muted_teal_theme)

        # phthalo green color
        self.phtahlo_green_btn = toolbar.addAction('Phthalo Green')
        self.phtahlo_green_btn.setIcon(QIcon(
            'C:/Users/1973r/OneDrive/Desktop/PyQt_apps/CalmIris/toolbar_icons/phthalo_green'))
        self.phtahlo_green_btn.setToolTip('Phthalo Green')
        self.phtahlo_green_btn.triggered.connect(self.apply_phthalo_green)

        # navy blue
        self.navy_blue_btn = toolbar.addAction('Nave Blue')
        self.navy_blue_btn.setIcon(QIcon(
            'C:/Users/1973r/OneDrive/Desktop/PyQt_apps/CalmIris/toolbar_icons/navy_blue.png'))
        self.navy_blue_btn.setToolTip('Navy Blue')
        self.navy_blue_btn.triggered.connect(self.apply_navy_blue_theme)

        # reddish-brown
        self.reddish_brown = toolbar.addAction('Reddist Brown')
        self.reddish_brown.setIcon(QIcon(
            'C:/Users/1973r/OneDrive/Desktop/PyQt_apps/CalmIris/toolbar_icons/reddish_brown.png'))
        self.reddish_brown.setToolTip('Reddish Brown')
        self.reddish_brown.triggered.connect(self.apply_reddish_brown_theme)

        # rich golden-yellow
        self.golden_yellow = toolbar.addAction('Golden Yellow')
        self.golden_yellow.setIcon(QIcon(
            'C:/Users/1973r/OneDrive/Desktop/PyQt_apps/CalmIris/toolbar_icons/golden_yellow.png'))
        self.golden_yellow.setToolTip('Golden Yellow')
        self.golden_yellow.triggered.connect(self.apply_golden_yellow_theme)

        # dark olive green
        self.dark_olive_green = toolbar.addAction('Dark Olive Green')
        self.dark_olive_green.setIcon(QIcon(
            'C:/Users/1973r/OneDrive/Desktop/PyQt_apps/CalmIris/toolbar_icons/dark_olive_green.png'))
        self.dark_olive_green.setToolTip('Dark Olive Green')
        self.dark_olive_green.triggered.connect(
            self.apply_dark_olive_green_theme)

        # bright lime green
        self.bright_lime_green = toolbar.addAction('Bright Lime Green')
        self.bright_lime_green.setIcon(QIcon(
            'C:/Users/1973r/OneDrive/Desktop/PyQt_apps/CalmIris/toolbar_icons/bright_lime_green.png'))
        self.bright_lime_green.setToolTip('Bright Lime Green')
        self.bright_lime_green.triggered.connect(
            self.apply_bright_lime_green_theme)

        # dark crimson red
        self.dark_crimson_red = toolbar.addAction('Dark Crimson Red')
        self.dark_crimson_red.setIcon(QIcon(
            'C:/Users/1973r/OneDrive/Desktop/PyQt_apps/CalmIris/toolbar_icons/dark_crimson_red.png'))
        self.dark_crimson_red.setToolTip('Dark Crimson Red')
        self.dark_crimson_red.triggered.connect(self.apply_dark_crimson_red)

        # dark purple shade
        self.dark_purple_shade = toolbar.addAction('Dark Purple Shade')
        self.dark_purple_shade.setIcon(QIcon(
            'C:/Users/1973r/OneDrive/Desktop/PyQt_apps/CalmIris/toolbar_icons/dark_purple_shade.png'))
        self.dark_purple_shade.setToolTip('Dark Purple Shade')
        self.dark_purple_shade.triggered.connect(
            self.apply_dark_purple_shade_theme)

        # extremely dark purple
        self.extreme_dark_purple = toolbar.addAction('Extreme Dark Purple')
        self.extreme_dark_purple.setIcon(QIcon(
            'C:/Users/1973r/OneDrive/Desktop/PyQt_apps/CalmIris/toolbar_icons/extreme_dark_purple.png'))
        self.extreme_dark_purple.setToolTip('Extreme Dark Purple')
        self.extreme_dark_purple.triggered.connect(
            self.apply_extreme_dark_purple_theme)

        # light golden tan
        self.light_golden_tan = toolbar.addAction('Light Golden Tan')
        self.light_golden_tan.setIcon(QIcon(
            'C:/Users/1973r/OneDrive/Desktop/PyQt_apps/CalmIris/toolbar_icons/light_golden_tan.png'))
        self.light_golden_tan.setToolTip('Light Golden Tan')
        self.light_golden_tan.triggered.connect(
            self.apply_light_golden_tan_theme)

        # soft, warm beige
        self.soft_warm_beige = toolbar.addAction('Soft Warm Beige')
        self.soft_warm_beige.setIcon(QIcon(
            'C:/Users/1973r/OneDrive/Desktop/PyQt_apps/CalmIris/toolbar_icons/soft_warm_beige.png'))
        self.soft_warm_beige.setToolTip('Soft Warm Beige')
        self.soft_warm_beige.triggered.connect(
            self.apply_soft_warm_beige_theme)

        # earthy shade brown
        self.earth_shade_brown = toolbar.addAction('Earthy shade Brown')
        self.earth_shade_brown.setIcon(QIcon(
            'C:/Users/1973r/OneDrive/Desktop/PyQt_apps/CalmIris/toolbar_icons/earthy_shade_brown.png'
        ))
        self.earth_shade_brown.setToolTip('Earthy Shade Brown')
        self.earth_shade_brown.triggered.connect(
            self.apply_earthy_shade_brown_theme)

        # very light shade of gray
        self.very_light_shade_gray = toolbar.addAction(
            'Very Light Shade of Gray')
        self.very_light_shade_gray.setIcon(QIcon(
            'C:/Users/1973r/OneDrive/Desktop/PyQt_apps/CalmIris/toolbar_icons/very_light_shade_gray.png'
        ))
        self.very_light_shade_gray.setToolTip('Very Light Shade of Gray')
        self.very_light_shade_gray.triggered.connect(
            self.apply_very_light_shade_theme)

        # muted shade of grayish blue
        self.muted_shade_grayish_blue = toolbar.addAction(
            'Muted Shade of Grayish Blue')
        self.muted_shade_grayish_blue.setIcon(QIcon(
            'C:/Users/1973r/OneDrive/Desktop/PyQt_apps/CalmIris/toolbar_icons/muted_shade_grayish_blue.png'
        ))
        self.muted_shade_grayish_blue.setToolTip('Muted Shade of Grayish Blue')
        self.muted_shade_grayish_blue.triggered.connect(
            self.apply_muted_shade_grayish_blue_theme
        )

        # rich shade of burgundy
        self.rich_shade_burgundy = toolbar.addAction('Rich Shade of Burgundy')
        self.rich_shade_burgundy.setIcon(QIcon(
            'C:/Users/1973r/OneDrive/Desktop/PyQt_apps/CalmIris/toolbar_icons/rich_shade_of_burgundy.png'
        ))
        self.rich_shade_burgundy.setToolTip('Rich Shade of Burgundy')
        self.rich_shade_burgundy.triggered.connect(
            self.apply_rich_sade_of_burgundy_theme
        )

        # Dusky Forest Gradient
        self.dusky_forest_gradient = toolbar.addAction(

            'Dusky Forest Gradient')
        self.dusky_forest_gradient.setIcon(QIcon(
            'C:/Users/1973r/OneDrive/Desktop/PyQt_apps/CalmIris/toolbar_icons/Dusky_forest_gradient.png'
        ))
        self.dusky_forest_gradient.setToolTip('Dusky Forest Gradient')
        self.dusky_forest_gradient.triggered.connect(
            self.apply_dusky_forest_gradient_theme
        )

        # Cosmic Twilight
        self.cosmic_twilight = toolbar.addAction('Cosmic Twilight')
        self.cosmic_twilight.setIcon(QIcon(
            'C:/Users/1973r/OneDrive/Desktop/PyQt_apps/CalmIris/toolbar_icons/cosmic_twilight.png'
        ))
        self.cosmic_twilight.setToolTip('Cosmic Twilight')
        self.cosmic_twilight.triggered.connect(
            self.apply_cosmic_twilight_gradient_theme
        )

        # Autumn Ember
        self.autumn_ember = toolbar.addAction('Autumn Ember')
        self.autumn_ember.setIcon(QIcon(
            'C:/Users/1973r/OneDrive/Desktop/PyQt_apps/CalmIris/toolbar_icons/Autumn_Ember.png'
        ))
        self.autumn_ember.setToolTip('Autumn Ember')
        self.autumn_ember.triggered.connect(
            self.apply_autumn_ember_theme
        )

        # Pine Tree
        self.pine_tree = toolbar.addAction('Pine Tree')
        self.pine_tree.setIcon(QIcon(
            'C:/Users/1973r/OneDrive/Desktop/PyQt_apps/CalmIris/toolbar_icons/Pine_Tree.png'
        ))
        self.pine_tree.setToolTip('Pine Tree')
        self.pine_tree.triggered.connect(
            self.apply_pine_tree_theme
        )
        # Neon Velvet Gradient
        self.Neon_velvet_gradient = toolbar.addAction('Neon Velvet Gradient')
        self.Neon_velvet_gradient.setIcon(QIcon(
            'C:/Users/1973r/OneDrive/Desktop/PyQt_apps/CalmIris/toolbar_icons/neon_velvet_gradient.png'))
        self.Neon_velvet_gradient.setToolTip('Neon Velvet Gradient')
        self.Neon_velvet_gradient.triggered.connect(
            self.apply_neon_velvet_gradient_theme)

        # Rustic Coffee Gradient
        self.rustic_coffee_gradient = toolbar.addAction(
            'Rustic Coffee Gradient')
        self.rustic_coffee_gradient.setIcon(QIcon(
            'C:/Users/1973r/OneDrive/Desktop/PyQt_apps/CalmIris/toolbar_icons/rustic_coffee_gradient.png'))
        self.rustic_coffee_gradient.setToolTip('Rustic Coffee Gradient')
        self.rustic_coffee_gradient.triggered.connect(
            self.apply_rustic_coffee_gradient_theme)

        # Dark Cyan Grove Gradient
        self.dark_cyan_grove_gradient = toolbar.addAction(
            'Dark Cyan Grove Gradient')
        self.dark_cyan_grove_gradient.setIcon(QIcon(
            'C:/Users/1973r/OneDrive/Desktop/PyQt_apps/CalmIris/toolbar_icons/dark_cyan_grove_gradient.png'))
        self.dark_cyan_grove_gradient.setToolTip('Dark Cyan Grove Gradient')
        self.dark_cyan_grove_gradient.triggered.connect(
            self.apply_dark_cyan_grove_gradient_theme)

        # Mossy Gold Gradient
        self.mossy_gold_gradient = toolbar.addAction('Mossy Gold Gradient')
        self.mossy_gold_gradient.setIcon(QIcon(
            'C:/Users/1973r/OneDrive/Desktop/PyQt_apps/CalmIris/toolbar_icons/mossy_gold_gradient.png'))
        self.mossy_gold_gradient.setToolTip('Mossy Gold Gradient')
        self.mossy_gold_gradient.triggered.connect(
            self.apply_mossy_gold_gradient_theme)

        # Regal Plum Gradient
        self.regal_plum_gradient = toolbar.addAction('Regal Plum Gradient')
        self.regal_plum_gradient.setIcon(QIcon(
            'C:/Users/1973r/OneDrive/Desktop/PyQt_apps/CalmIris/toolbar_icons/regal_plum_gradient.png'))
        self.regal_plum_gradient.setToolTip('Regal Plum Gradient')
        self.regal_plum_gradient.triggered.connect(
            self.apply_regal_plum_gradient_theme)

        # Deep Crimson Red
        self.deep_crimson_red = toolbar.addAction('Deep Crimson Red')
        self.deep_crimson_red.setIcon(QIcon(
            'C:/Users/1973r/OneDrive/Desktop/PyQt_apps/CalmIris/toolbar_icons/deep_crimson_red_gradient.png'))
        self.deep_crimson_red.setToolTip('Deep Crimson Red')
        self.deep_crimson_red.triggered.connect(
            self.apply_deep_crimson_red_theme)

        # Midnight Fog Gradient
        self.midnight_fog_gradient = toolbar.addAction('Midnight Fog Gradient')
        self.midnight_fog_gradient.setIcon(QIcon(
            'C:/Users/1973r/OneDrive/Desktop/PyQt_apps/CalmIris/toolbar_icons/midnight_fog_gradient.png'))
        self.midnight_fog_gradient.setToolTip('Midnight Fog Gradient')
        self.midnight_fog_gradient.triggered.connect(
            self.apply_midnight_fog_gradient_theme)

        # Rustic Ocean Gradient
        self.rustic_ocean_gradient = toolbar.addAction('Rustic Ocean Gradient')
        self.rustic_ocean_gradient.setIcon(QIcon(
            'C:/Users/1973r/OneDrive/Desktop/PyQt_apps/CalmIris/toolbar_icons/rustic_ocean_gradient.png'))
        self.rustic_ocean_gradient.setToolTip('Rustic Ocean Gradient')
        self.rustic_ocean_gradient.triggered.connect(
            self.apply_rustic_ocean_gradient_theme)

        # Dark Velvet Gradient
        self.dark_velvet_gradient = toolbar.addAction('Dark Velvet Gradient')
        self.dark_velvet_gradient.setIcon(QIcon(
            'C:/Users/1973r/OneDrive/Desktop/PyQt_apps/CalmIris/toolbar_icons/dark_vevlet_gradient.png'))
        self.dark_velvet_gradient.setToolTip('Dark Velvet Gradient')
        self.dark_velvet_gradient.triggered.connect(
            self.apply_dark_velvet_gradient_theme
        )

        # Color picker
        self.color_picker = toolbar.addAction('Color Picker')
        self.color_picker.setIcon(QIcon(
            'C:/Users/1973r/OneDrive/Desktop/PyQt_apps/CalmIris/toolbar_icons/color_picker.png'
        ))
        self.color_picker.setToolTip('Pick colors')
        self.color_picker.triggered.connect(self.open_color_picker)

    # display all colors on label -------------------------------------------------------------------------------------
    def apply_phthalo_green(self):
        self.setStyleSheet("""
            QMainWindow{
                background-color: qlineargradient(x1: 0, x2: 1, stop: 0 #5B8373, stop: 1 #027044);
                
            }               
            
            #label {
                background-color : #123024;
                border-radius: 10px;
            }""")

    def apply_mint_green_btn(self):
        self.setStyleSheet("""
            QMainWindow{
                background-color: qlineargradient(x1: 0, x2: 1, stop: 0 #014224, stop: 1 #15ED89);
                
            }               
            
            #label {
                background-color : #52B788;
                color: f000000;
                border-radius: 10px;
            }
                           """)

    def apply_muted_teal_theme(self):
        self.setStyleSheet("""
            QMainWindow{
                background-color: qlineargradient(x1: 0, x2: 1, stop: 0 #202322, stop: 1 #012D27);
                
            }               
            
            #label {
                background-color: #2e4542;
                border-radius: 10px;
                }""")

    def apply_sky_blue_theme(self):
        self.setStyleSheet("""_
            QMainWindow{
                background-color: qlineargradient(x1: 0, x2: 1, stop: 0 #020235, stop: 1 #01454F);
                
            }               
            
            #label {
                background-color : #035A8C;
                border-radius: 10px;
            }
        """)

    def apply_navy_blue_theme(self):
        self.setStyleSheet("""
            QMainWindow{
                background-color: qlineargradient(x1: 0, x2: 1, stop: 0 #040E82, stop: 1 #545884);
                
            }               
            
            #label {
                background-color : #05082b;
                border-radius: 10px;
            }""")

    def apply_reddish_brown_theme(self):
        self.setStyleSheet("""
            QMainWindow{
                background-color: qlineargradient(x1: 0, x2: 1, stop: 0 #5E0401, stop: 1 #BE423E);
                
            }               
            
            #label {
                background-color : #2b0503;
                border-radius: 10px;
            }""")

    def apply_golden_yellow_theme(self):
        self.setStyleSheet("""
            QMainWindow{
                background-color: qlineargradient(x1: 0, x2: 1, stop: 0 #352403, stop: 1 #B07808);
                
            }               
            
            #label {
                background-color : #d79f02;
                border-radius: 10px;
            }      
            """)

    def apply_dark_olive_green_theme(self):
        self.setStyleSheet("""
            QMainWindow{
                background-color: qlineargradient(x1: 0, x2: 1, stop: 0 #78773D, stop: 1 #222103);
                
            }               
            
            #label {
                background-color : #555410;
                border-radius: 10px;
                }
            """)

    def apply_bright_lime_green_theme(self):
        self.setStyleSheet("""
            QMainWindow{
                background-color: qlineargradient(x1: 0, x2: 1, stop: 0 #4C7402, stop: 1 #A7C572);
                
            }               
            
            #label {
                background-color : #aec405;
                color: f000000;
                border-radius: 10px;
                }
            """)

    def apply_dark_crimson_red(self):
        self.setStyleSheet("""
            QMainWindow{
                background-color: qlineargradient(x1: 0, x2: 1, stop: 0 #A50101, stop: 1 #362121);
                
            }               
            
            #label {
                background-color : #5c0b0b;
                border-radius: 10px;
                }
            """)

    def apply_dark_purple_shade_theme(self):
        self.setStyleSheet("""
            QMainWindow{
                background-color: qlineargradient(x1: 0, x2: 1, stop: 0 #180722, stop: 1 #5C3374);
                
            }               
            
            #label {
                background-color : #5A3985;
                border-radius: 10px;
                }
                           """)

    def apply_extreme_dark_purple_theme(self):
        self.setStyleSheet("""
            QMainWindow{
                background-color: qlineargradient(x1: 0, x2: 1, stop: 0 #47017D, stop: 1 #8C08F0);
                
            }               
            
            #label {
                background-color : #150620;
                border-radius: 10px;
                }""")

    def apply_light_golden_tan_theme(self):
        self.setStyleSheet("""     
            QMainWindow{
                background-color: qlineargradient(x1: 0, x2: 1, stop: 0 #5A3A02, stop: 1 #FAD492);
                
            }               
            
            #label {
                background-color : #d6b986;
                border-radius: 10px;
                color: f000000;
                }
                           """)

    def apply_soft_warm_beige_theme(self):
        self.setStyleSheet("""
            QMainWindow{
                background-color: qlineargradient(x1: 0, x2: 1, stop: 0 #67533D, stop: 1 #865F36);
                
            }               
            
            #label {
                background-color : #e1cab2;
                border-radius: 10px;
                color: f000000;
                }""")

    def apply_earthy_shade_brown_theme(self):
        self.setStyleSheet("""
            QMainWindow{
                background-color: qlineargradient(x1: 0, x2: 1, stop: 0 #32190A, stop: 1 #312925);
                
            }               
            
            #label {
                background-color: #87624a;
                border-radius: 10px;
                }
                           """)

    def apply_very_light_shade_theme(self):
        self.setStyleSheet("""
            QMainWindow{
                background-color: qlineargradient(x1: 0, x2: 1, stop: 0 #403A3A, stop: 1 #161414);
                
            }               
            
            #label {
                background-color: #F0F0F0;
                color: f000000;
                border-radius: 10px;
                }
                           """)

    def apply_muted_shade_grayish_blue_theme(self):
        self.setStyleSheet("""
            QMainWindow{
                background-color: qlineargradient(x1: 0, x2: 1, stop: 0 #577A83, stop: 1 #303D41);
                
            }               
            
            #label {
                background-color: #bec2c3;
                color: f000000;
                border-radius: 10px;
                }
                           """)

    def apply_rich_sade_of_burgundy_theme(self):
        self.setStyleSheet("""
            QMainWindow{
                background-color: qlineargradient(x1: 0, x2: 1, stop: 0 #1D0E16, stop: 1 #32051B);
                
            }               
            
            #label {
                background-color: #33212a;
                border-radius: 10px;
                }""")

    def apply_dusky_forest_gradient_theme(self):
        self.setStyleSheet("""
         QMainWindow{
                background-color: #312119;
                
            }               
            
            #label {
            background-color: qlineargradient(x1: 0, x2: 1, 
            stop: 0 #03052b, 
            stop: 0.33 #0b2732, 
            stop: 0.66 #433203, 
            stop: 1 #32051B);

            border-radius: 10px;
                }
                           """)

    def apply_cosmic_twilight_gradient_theme(self):
        self.setStyleSheet("""
             QMainWindow{
                background-color: #07050F;
                
            }               
            
            #label {
                background-color: qlineargradient(x1: 0, x2: 1, 
                stop: 0 #20005b, 
                stop: 1 #010105);

                border-radius: 10px;
                }""")

    def apply_autumn_ember_theme(self):
        self.setStyleSheet("""
            QMainWindow{
                background-color: #4A2C0E;
                
            }               
            
            #label {
                background-color: qlineargradient(x1: 0, x2: 1, 
                stop: 0 #3f4016, 
                stop: 1 #5b0b00);

                border-radius: 10px;
                }
                           """)

    def apply_pine_tree_theme(self):
        self.setStyleSheet("""
            QMainWindow{
                background-color: #203511;
                
            }               
            
            #label {
                background-color: qlineargradient(x1: 0, x2: 1, 
                stop: 0 #078900, 
                stop: 1 #0c290a);

                border-radius: 10px;
                }""")

    def apply_neon_velvet_gradient_theme(self):
        self.setStyleSheet('''
            QMainWindow{
                background-color: #30103A;
                
            }               
            
            #label {
                background-color: qlineargradient(x1: 0, x2: 1, 
                stop: 0 #552ea1, 
                stop: 1 #ff66c4);

                border-radius: 10px;
                }
        
                           ''')

    def apply_rustic_coffee_gradient_theme(self):
        self.setStyleSheet('''
            QMainWindow{
                background-color: #3A1F10;
                
            }               
            
            #label {
                background-color: qlineargradient(x1: 0, x2: 1, 
                stop: 0 #140308, 
                stop: 1 #8d6520);

                border-radius: 10px;
                }''')

    def apply_dark_cyan_grove_gradient_theme(self):
        self.setStyleSheet('''
            QMainWindow{
                background-color: #14251A;
                
            }               
            
            #label {
                background-color: qlineargradient(x1: 0, x2: 1, 
                stop: 0 #00444d, 
                stop: 1 #0c4712);

                border-radius: 10px;
                }''')

    def apply_mossy_gold_gradient_theme(self):
        self.setStyleSheet('''
            QMainWindow{
                background-color: #3E531D;
                
            }               
            
            #label {
                background-color: qlineargradient(x1: 0, x2: 1, 
                stop: 0 #8f9200, 
                stop: 1 #1f4d1a);

                border-radius: 10px;
                }''')

    def apply_regal_plum_gradient_theme(self):
        self.setStyleSheet('''
            QMainWindow{
                background-color: #531D39;
                
            }               
            
            #label {
                background-color: qlineargradient(x1: 0, x2: 1, 
                stop: 0 #92008c, 
                stop: 1 #9f8308);

                border-radius: 10px;
                }''')

    def apply_deep_crimson_red_theme(self):
        self.setStyleSheet('''
                            QMainWindow{
                background-color: #220E0E;
                
            }               
            
            #label {
                background-color: qlineargradient(x1: 0, x2: 1, 
                stop: 0 #000000, 
                stop: 1 #920000);

                border-radius: 10px;
                }''')

    def apply_midnight_fog_gradient_theme(self):
        self.setStyleSheet('''
                            QMainWindow{
                background-color: #171515;
                
            }               
            
            #label {
                background-color: qlineargradient(x1: 0, x2: 1, 
                stop: 0 #0a0a0b, 
                stop: 1 #383a47);

                border-radius: 10px;
                }''')

    def apply_rustic_ocean_gradient_theme(self):
        self.setStyleSheet('''
                             QMainWindow{
                background-color: #21074B;
                
            }               
            
            #label {
                background-color: qlineargradient(x1: 0, x2: 1, 
                stop: 0 #003b89, 
                stop: 1 #5b2b20);

                border-radius: 10px;
                }
                           ''')

    def apply_dark_velvet_gradient_theme(self):
        self.setStyleSheet('''
                             QMainWindow{
                background-color: #160514;
                
            }               
            
            #label {
                background-color: qlineargradient(x1: 0, x2: 1, 
                stop: 0 #000000, 
                stop: 1 #40203c);

                border-radius: 10px;
                }''')

    def open_color_picker(self):

        pick_color = QColorDialog.getColor()
        self.setStyleSheet(
            f' #label{{background-color: {pick_color.name()}; border-radius: 10px}} QMainWindow{{background-color:rgb(26, 3, 48)}}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CalmIris_win()
    window.show()

    sys.exit(app.exec())
