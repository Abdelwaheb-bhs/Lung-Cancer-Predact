from flet import *
import shutil
import os
from flet.matplotlib_chart import MatplotlibChart
from methods import load_data
#from  simpledt import CSVDataTable



def main(page : Page):
    page.window_width=700
    page.window_height=800
    page.window_resizable = False
    page.scroll="always"
    page.padding=0
    page.spacing=0
    location=Text("")
    matriceFig=Container(content=Text("no data"))
    screeFig=Container(content=Text("no data"))
    graphFig=Container(content=Text("no data"))
    kmeanFig=Container(content=Text("no data"))
    chrFig=Container(content=Text("no data"))
    circleFig=Container(content=Text("no data"))
    eboliFig=Container(content=Text("no data"))
    dataTable=Container(content=Text("no data"),height=page.window_height/2,width=page.window_width-50)
    dataTable2=Container(content=Text("no data"),height=page.window_height/2,width=page.window_width-50)   
    dataTable3=Container(content=Text("no data"),height=page.window_height/2,width=page.window_width-50)   
     
    def dialog_picker(e:FilePickerResultEvent):
        for x in e.files:
            print(x.name)
            urCopy = os.path.join(os.getcwd(),"myUploads")
            shutil.copy(x.path,urCopy)
            location.value=f"{x.name}"
            #location.update()
            fig=load_data(x.name)
            matriceFig.content=MatplotlibChart(fig[0],expand=True)
            screeFig.content=MatplotlibChart(fig[1],expand=True)
            graphFig.content=MatplotlibChart(fig[2],expand=True)
            kmeanFig.content=MatplotlibChart(fig[3],expand=True)
            chrFig.content=MatplotlibChart(fig[4],expand=True)
            circleFig.content=MatplotlibChart(fig[5],expand=True)
            eboliFig.content=MatplotlibChart(fig[6],expand=True)
            dataTable.content=Row([Column([fig[7]],scroll="always")],scroll="always")
            csv=CSVDataTable("file.csv")
            table=csv.datatable
            dataTable2.content=Row([Column([table],scroll="always")],scroll="always")
            csv=CSVDataTable("file2.csv")
            table=csv.datatable
            dataTable3.content=Row([Column([table],scroll="always")],scroll="always")
            matriceFig.update()
            screeFig.update()
            graphFig.update()
            kmeanFig.update()
            chrFig.update()
            circleFig.update()
            dataTable.update()
            dataTable2.update()
            dataTable3.update()
            eboliFig.update()
            print(location.value)
            print(isinstance(location.value, str))
            page.update()
    
    def getName(pick:FilePicker):
        return pick.file_name
    
            
    showedScreen=Container(alignment=alignment.center,
                padding=15,
                content=Column([
                    Stack([Text("Lung Cancer\nData Analysis",font_family="Bebas Neue",size=30),
                    Image(
                        src="myUploads/bg.png",height=400,width=400
                    ),
                    ]),
                    
                    Text("An application that allows you to perform accurate analysis of samples and confirm the extent of their infection with this disease, as this application provides you with an illustrative display of these samples by uploading their file, and displaying specific charts for each analysis.")
                ],alignment=alignment.center))          
    def urChangeChoice(e):
        screenIndex = e.control.selected_index
        if screenIndex == 4 :
            showedScreen.content=myHome 
        elif screenIndex == 6 :
            showedScreen.content=Kmeans   
        elif screenIndex == 8 :
            showedScreen.content=Data 
        elif screenIndex == 10 :
            showedScreen.content = Acp        
        page.update()
    Mypick = FilePicker(on_result=dialog_picker)
    page.overlay.append(Mypick)
    Kmeans=Container(
        padding=15,
        content=Column([
            Text("vous devez attendre quelques secondes jusqu'au téléchargement des données"),
            Text("Tableau de données",weight=FontWeight.BOLD,size=30),
            Text("La base de données est composée de 309 lignes et 15 colonnes. Les 15 colonnes représentent différentes caractéristiques ou variables. Cependant les 309 lignes sont les observations.",size=16),
            Column([dataTable]),
            Text("la normalisation des données :",weight=FontWeight.BOLD,size=30),
            dataTable3,
            Text("Matrice de corrélation",weight=FontWeight.BOLD,size=30),
            Text("La matrice de corrélation est une représentation tabulaire des corrélations entre les différentes paires de variables dans la base de données.",size=16),
            matriceFig,
            Container(height=150)
        ])
    )
    
    page.theme = Theme(
    scrollbar_theme=ScrollbarTheme(
        
        thumb_visibility=True,
        thumb_color={
            MaterialState.HOVERED: "#ff5454",
            MaterialState.DEFAULT: "#ff5454",
        },
        thickness=4,
        radius=15,
        main_axis_margin=5,
        cross_axis_margin=10,
    )
)
    Data=Container(
        padding=15,
        content=Column([
            Text("Analyse en Composantes Principales",weight=FontWeight.BOLD,size=30),
            Text("vous devez attendre quelques secondes jusqu'au téléchargement des données"),
            Text("L'ACP est une technique qui vise à réduire la dimensionnalité des données en projetant les observations dans un nouvel espace de variables, appelées composantes principales. ",size=16),
            Text("Tableau de données avec l'ACP",weight=FontWeight.BOLD,size=30),
            dataTable2,
            Text("L'ACP normée est une variante où les données sont centrées et réduites (normalisées) avant d'appliquer l'ACP",size=16),
            Text("l’éboulis des valeurs propres (scree plot)",weight=FontWeight.BOLD,size=30),
            screeFig,
            Text("Graphique des Variances Cumulées Expliquées",weight=FontWeight.BOLD,size=30),
            graphFig,
            Text("l’éboulis des valeurs propres",),
            Text("Le pourcentage d'inertie mesure la proportion de la variance totale des données expliquée par chaque composante principale. L'éboulis des valeurs propres nous permet de visualiser cette information. Les composantes principales avec des valeurs propres élevées (proches de 1) expliquent une grande partie de la variance des données.",size=16),
            eboliFig,
            Text("La saturation des variables représente la corrélation entre les variables initiales et les composantes principales. Un cercle de corrélation est tracé pour visualiser cette relation. ",size=16),
            Text("Cercle de corrélation",weight=FontWeight.BOLD,size=30),
            Text("Les variables qui sont proches du cercle ont une forte contribution à la composante principale correspondante",size=16),
            circleFig,
            Container(height=150)
            
        ],scroll="always",on_scroll_interval=0)
        
    )
    
    page.update()
    
    Acp=Container(
        padding=15,
                content=Column([
                    Text("vous devez attendre quelques secondes jusqu'au téléchargement des données"),
                    Text("K-means",weight=FontWeight.BOLD,size=30),
                    Text("Le K-means est un algorithme de clustering non supervisé largement utilisé pour diviser un ensemble de données en un nombre prédéfini de groupes, appelés clusters.",size=16),
                    Text("K-means Clustering",weight=FontWeight.BOLD,size=30),
                    Text("Dans ce cas, nous l'appliquons pour diviser les données en deux classes, ce qui peut correspondre, par exemple, aux sujets malades et sains. Les centres de chaque cluster, appelés centroïdes, sont déterminés par l'algorithme.",size=16),
                    kmeanFig,
                    Text("Classification Ascendante Hiérarchique",weight=FontWeight.BOLD,size=30),
                    Text("La CAH est un autre algorithme de clustering non supervisé qui crée une hiérarchie de clusters.",size=16),
                    Text("Hierarchical Clustering Dendrogram",weight=FontWeight.BOLD,size=30),
                    chrFig,
                    Container(height=150)
                    
                    
                    
                ])
            )
    page.update()
    myHome=Container(
                
                alignment=alignment.center,
                padding=15,
                content=Column([
                    Stack([Text("Lung Cancer\nData Analysis",font_family="Bebas Neue",size=30),
                    Image(
                        src="myUploads/bg.png",height=400,width=400
                    ),
                    ]),
                    
                    Text("An application that allows you to perform accurate analysis of samples and confirm the extent of their infection with this disease, as this application provides you with an illustrative display of these samples by uploading their file, and displaying specific charts for each analysis.")
                ],alignment=alignment.center)
                
            )
    myTab = Tabs(
        selected_index=0,
        animation_duration=300,
        indicator_color="white",
        divider_color="#27472f",
        label_color="white",
        scrollable=True,
        on_change=urChangeChoice,
        tabs=[
            Container(expand=True),
            Container(expand=True),
            Container(expand=True),
            Container(expand=True),
            Tab(text="HOME"),
            Container(expand=True),
            Tab(text="Data"),
            Container(expand=True),
            Tab(text="ACP"),
            Container(expand=True),
            Tab(text="K means")

        ]
    )
    myBar=Stack(
            [
                Row([ Container(
        shadow=BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color="#008166"
        ),
        gradient =   LinearGradient(
                begin=alignment.top_left,
                end=alignment.bottom_right,
                colors=["#00d5ac","#00ac89"]
            ),
        margin=margin.only(
            top=page.window_height-130,
            left=10,
            right=10
        ),
        border_radius=30,
        width=page.window_width-40,
        padding=10,
        content=myTab


    )],alignment=alignment.center),
                Container(
                    
                    margin=margin.only(
                        top=page.window_height-230,
                        left=page.window_width/2-33,
                        right=page.window_width/2-35
                    ),
                    bgcolor="#ff5454",
                    border=border.all(5,"white"),
                    shape=BoxShape.CIRCLE,
                    content=GestureDetector(
                        mouse_cursor=MouseCursor.CLICK,
                        on_tap=lambda _: Mypick.pick_files(),
                        content=Container(alignment=alignment.center,content=Icon(name="add",size=40,color="white"))
                    )
                )
            ],
        )
    
    page.overlay.append(myBar)
    page.add(
        Stack([
            
            showedScreen
            
        ])
    )
app(target=main,assets_dir="myUploads",upload_dir="myUploads")