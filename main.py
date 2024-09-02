import flet as ft

def main(page: ft.Page):
	page.bgcolor = ft.colors.BLACK
	page.horizontal_alignment = ft.CrossAxisAlignment.CENTER	
	page.vertical_alignment = ft.MainAxisAlignment.CENTER
	page.padding = ft.padding.all(30)
	page.window_min_height = 700
	page.window_min_width = 800

	def chair1(e):
		image_main.src = 'images/chair_1.png'
		image_main.update()

	def chair2(e):
		image_main.src = 'images/chair_2.png'
		image_main.update()

	def chair3(e):
		image_main.src = 'images/chair_3.png'
		image_main.update()

	content_descricao = ft.Container(
		content = ft.Text(
			value = 'A escolha de uma cadeira adequada é muito importante para evitar futuras lesões. Com esta cadeira da ThunderX3 você terá o conforto é o bem-estar que precisa ao longo do seu dia. Além disso, você pode colocá-la em qualquer lugar da sua casa ou oficina, pois o seu design se adapta a vários ambientes. Dê um toque mais moderno aos seus espaços!',
			style = ft.TextStyle(
				size = 10,
				weight = ft.FontWeight.NORMAL,
				color = ft.colors.WHITE70
			),
			text_align = ft.TextAlign.LEFT
		),
		padding = ft.padding.symmetric(vertical = 10)
	)

	content_detalhes = ft.Container(
		content = ft.Text(
			value = 'Modelo: TGC12 - Cor: Vermelha - Dimensões: Encosto (L x A): 57 x 82 cm | Braços (L x A): 66 x 61-78 cm - Material: poliuretano, metal, nylon, espuma - Espuma: alta densidade - Mecanismo padrão: borboleta - Moldura: metal - Base: metal - Rodinhas: Nylon, 65mm - Peso: 21 kg - Garantia: 06 meses (03 meses de garantia legal do CDC + 03 meses de período de cortesia concedido pela marca)',
			style = ft.TextStyle(
				size = 10,
				weight = ft.FontWeight.NORMAL,
				color = ft.colors.WHITE70
			),
			text_align = ft.TextAlign.LEFT
		),
		padding = ft.padding.symmetric(vertical = 10)
	)

	box_images = ft.Container(
		col = {'xs': 12, 'md': 6},
		bgcolor = ft.colors.WHITE,
		margin = ft.margin.all(0),
		padding = ft.padding.all(20),
		content = ft.Column(
			alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
			horizontal_alignment = ft.CrossAxisAlignment.CENTER,
			spacing = 0,
			controls = [
				image_main := ft.Image(src = 'images/chair_1.png', height = 250),
				ft.Divider(height = 100, color = ft.colors.TRANSPARENT),
				ft.ResponsiveRow(
					alignment = ft.MainAxisAlignment.SPACE_EVENLY,					
					controls = [
						ft.Container(col=4, content = ft.Image(src = 'images/chair_1.png', height = 50), on_click = chair1),
						ft.Container(col=4, content = ft.Image(src = 'images/chair_2.png', height = 50), on_click = chair2),
						ft.Container(col=4, content = ft.Image(src = 'images/chair_3.png', height = 50), on_click = chair3),
					],
				)
			],
		)
	)

	box_descriptions = ft.Container(
		expand = True,
		col = {'xs': 12, 'md': 6},
		bgcolor = ft.colors.BLACK,
		margin = ft.margin.all(0),
		padding = ft.padding.all(20),
		content = ft.Column(
			controls = [
				categoria := ft.Text(
					value = 'CADEIRAS', 
					style = ft.TextStyle(
						size = 10, 
						weight = ft.FontWeight.BOLD,
						color = ft.colors.RED
					)
				),
				produto := ft.Text(
					value = 'Cadeira Gamer TGC12 ThunderX3 Vermelha',
					style = ft.TextStyle(
						size = 20,
						weight = ft.FontWeight.BOLD,
						color = ft.colors.WHITE
					) 
				),
				departamento := ft.Text(
					value = 'Setup Gamer',
					style = ft.TextStyle(
						size = 10,
						weight = ft.FontWeight.NORMAL,
						italic = True,
						color = ft.colors.WHITE70
					)
				),
				ft.ResponsiveRow(
					columns = 12,
					controls = [
						ft.Row(
							col = 5,
							controls = [
								ft.Text(
									value = 'R$',
									style = ft.TextStyle(
										size = 20,
										weight = ft.FontWeight.W_400,
										color = ft.colors.WHITE
									)
								),
								preco := ft.Text(
									value = '999,90',
									style = ft.TextStyle(
										size = 20,
										weight = ft.FontWeight.W_400,
										color = ft.colors.WHITE
									)
								),
							],
						),
						ft.Row(
							col = 6,
							controls = [
								ft.Icon(
									name = ft.icons.STAR,
									color = ft.colors.AMBER if _ < 4 else ft.colors.WHITE,
									size = 20
								) for _ in range(5)
							],
							spacing = 3
						)
					],
					alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
					vertical_alignment = ft.CrossAxisAlignment.CENTER
				),
				ft.Tabs(
					tabs = [
						ft.Tab(
							text = 'Descrição',
							content = content_descricao
						),
						ft.Tab(
							text = 'Detalhes',
							content = content_detalhes
						),
					],
					selected_index=0,
					animation_duration=300,
					divider_color=ft.colors.GREY_700,
					indicator_border_radius=ft.border.all(10),
					indicator_color=ft.colors.RED,
					indicator_tab_size=False,
					label_color=ft.colors.RED,
					unselected_label_color=ft.colors.WHITE70,
					scrollable=False,
					height = 150
				),
				ft.ResponsiveRow(
					columns = 12,
					controls = [
						ft.Dropdown(
							col = 6,
							label = 'Cor',
							options = [
								ft.dropdown.Option(key = 1, text = 'Vermelho'),
								ft.dropdown.Option(key = 2, text = 'Azul'),
								ft.dropdown.Option(key = 3, text = 'Verde'),
								ft.dropdown.Option(key = 4, text = 'Amarelo'),
							],
							filled = False,
							border = ft.InputBorder.OUTLINE,
							border_color = ft.colors.WHITE70,
							border_width=1,
            				border_radius=ft.border_radius.all(5),
							content_padding=10,
							text_size = 12,
							label_style = ft.TextStyle(size = 12, color = ft.colors.WHITE),
						),
						ft.Dropdown(
							col = 6,
							label = 'Quantidade',
							options = [
								ft.dropdown.Option(key = 1, text = '1'),
								ft.dropdown.Option(key = 2, text = '2'),
								ft.dropdown.Option(key = 3, text = '3'),
								ft.dropdown.Option(key = 4, text = '4'),
							],
							filled = False,
							border = ft.InputBorder.OUTLINE,
							border_color = ft.colors.WHITE70,
							border_width=1,
            				border_radius=ft.border_radius.all(5),
							content_padding=10,
							text_size = 12,
							label_style = ft.TextStyle(size = 12, color = ft.colors.WHITE),
						),
						
					],
				),
				ft.Container(expand = True),
				ft.ElevatedButton(
					text = 'Adicionar à lista de desejos',
					width = 900,
					style = ft.ButtonStyle(
						padding = ft.padding.all(10),
						color = {
							ft.MaterialState.DEFAULT: ft.colors.WHITE,
							ft.MaterialState.HOVERED: ft.colors.BLACK,
						},
						bgcolor = {
							ft.MaterialState.DEFAULT: ft.colors.TRANSPARENT,
							ft.MaterialState.HOVERED: ft.colors.WHITE,
						},
						side = {
							ft.MaterialState.DEFAULT: ft.BorderSide(width = 2, color = ft.colors.WHITE),
						}
						
					),
				),
				ft.ElevatedButton(
					text = 'Adicionar ao carrinho',
					width = 900,
					style = ft.ButtonStyle(
						padding = ft.padding.all(10),
						color = {
							ft.MaterialState.DEFAULT: ft.colors.BLACK,
							ft.MaterialState.HOVERED: ft.colors.WHITE,
						},
						bgcolor = {
							ft.MaterialState.DEFAULT: ft.colors.RED,
						},
						side = {
							ft.MaterialState.DEFAULT: ft.BorderSide(width = 2, color = ft.colors.RED),
						}
						
					),
				),
			],
			horizontal_alignment = ft.CrossAxisAlignment.START
		)
	)
	
	layout = ft.Container(
		bgcolor = ft.colors.WHITE,
		height = 500,
		width = 600,
		shadow = ft.BoxShadow(blur_radius = 75, color = ft.colors.TEAL),
		padding = ft.padding.all(0),
		content = ft.ResponsiveRow(
			columns = 12,
			expand = True,
			controls = [
				box_images,
				box_descriptions
			],
		)
	)
	
	page.add(layout)

if __name__ == '__main__':
	ft.app(target = main, assets_dir = 'assets')
