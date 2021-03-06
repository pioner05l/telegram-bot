import telebot
from telebot import types

#5347391121:AAEjM5jcSh_J75pvPhkDfHdYCC0hYQB_1kU

bot = telebot.TeleBot('5347391121:AAEjM5jcSh_J75pvPhkDfHdYCC0hYQB_1kU')



def create_keyboard():

	keyboard = types.InlineKeyboardMarkup()

	aries_btn = types.InlineKeyboardButton(text='Овен', callback_data='1')
	taurus_btn = types.InlineKeyboardButton(text='Телец', callback_data='2')
	gemini_btn = types.InlineKeyboardButton(text='Близнецы', callback_data='3')
	cancer_btn = types.InlineKeyboardButton(text='Рак', callback_data='4')
	leo_btn = types.InlineKeyboardButton(text='Лев', callback_data='5')
	virgo_btn = types.InlineKeyboardButton(text='Дева', callback_data='6')
	libra_btn = types.InlineKeyboardButton(text='Весы', callback_data='7')
	scorpio_btn = types.InlineKeyboardButton(text='Скорпион', callback_data='8')
	sagittarius_btn = types.InlineKeyboardButton(text='Стрелец', callback_data='9')
	capricorn_btn = types.InlineKeyboardButton(text='Козерог', callback_data='10')
	aquarius_btn = types.InlineKeyboardButton(text='Водолей', callback_data='11')
	pisces_btn = types.InlineKeyboardButton(text='Рыбы', callback_data='12')
	keyboard.add(aries_btn, taurus_btn, gemini_btn, cancer_btn, leo_btn, virgo_btn, libra_btn, scorpio_btn, sagittarius_btn, capricorn_btn, aquarius_btn, pisces_btn)
	return keyboard

@bot.message_handler(commands=['start'])
def start_bot(message):
	keyboard=create_keyboard()
	bot.send_message(message.chat.id, "Хочешь узнать свой гороскоп? Выбери свой знак зодиака", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	keyboard = create_keyboard()
	if call.message:
		if call.data == '1':
			img = open('images1.jpg', 'rb')
			bot.send_photo(chat_id=call.message.chat.id, photo=img)

			bot.send_message(chat_id=call.message.chat.id,
							 text='''Гороскоп на месяц: Овен: В начале июня стоит настроиться на серьезный лад. 
							 У вас будет шанс сделать многое для достижения каких-то важных целей, добиться 
							 больших перемен в жизни. Но вы можете упустить такие возможности, если будете легкомысленны, 
							 станете отвлекаться на пустяки или предпочтете рассчитывать на то, что все удачно сложится 
							 самой собой. Нужно будет проявить целеустремленность и настойчивость. 
							 Не исключено, что придется отложить какие-то запланированные развлечения, поездки и отдых,
							  чтобы сосредоточиться на решении неожиданно возникших задач. Вторая половина месяца 
							  сложится иначе. В это время многим вашим начинаниям будет сопутствовать удача. 
							  Найдется применение вашим знаниям и талантам – не исключено, что вы поймете, как превратить 
							  свое хобби в источник дополнительных доходов. Люди, с которыми вы прежде сотрудничали, 
							  могут предложить что-то интересное. У некоторых Овнов будет шанс подняться по карьерной 
							  лестнице, значительно укрепить свои профессиональные позиции. Забот будет немало, 
							  но останется время и для отдыха, общения с близкими и семейных дел.''')

		if call.data == '2':
			img = open('download2.jpg', 'rb')
			bot.send_photo(chat_id=call.message.chat.id, photo=img)

			bot.send_message(chat_id=call.message.chat.id,
							 text='''Гороскоп на месяц: Телец: Начало июня будет очень благоприятным для общения. Вам
							  станет заметно проще ладить с теми, кого вы еще недавно с трудом понимали. Удастся положить
							   конец разногласиям и спорам, помириться с теми, с кем вы были в ссоре. И деловые, и личные
							    отношения будут складываться гармонично. У вас появятся и новые союзники, и настоящие друзья.
							    Подойдет это время и для работы, решения новых задач. Вы быстро во всем разберетесь, поймете, 
							    как лучше действовать. Решения, принятые в первой половине месяца, хорошо скажутся на развитии 
							    вашей карьеры. Некоторые Тельцы найдут способ заметно увеличить доходы.
								Вторая половина месяца – отличное время для того, чтобы проявить инициативу. Это касается 
								всех сфер жизни: беритесь за новое, меняйте то, что вам не по душе, делитесь своими идеями 
								с теми, кому они могут быть интересны. Вы получите поддержку даже от тех, кто прежде никогда 
								не был на вашей стороне.''')

		if call.data == '3':
			img = open('download3.jpg', 'rb')
			bot.send_photo(chat_id=call.message.chat.id,photo=img)

			bot.send_message(chat_id=call.message.chat.id,
							 text='''Гороскоп на месяц: Близнецы: Начало июня будет насыщенным. Вам предстоит многое сделать, 
							 и не все сразу будет получаться хорошо. На пути могут возникать преграды, но они не заставят вас 
							 отступить. Не исключено, что в это время вам нужно будет сосредоточиться на работе, чтобы добиться 
							 заметного профессионального успеха. Деловые отношения будут складываться гармонично, у вас появятся 
							 новые союзники и партнеры, которые со временем станут вашими настоящими друзьями.
							 Подойдет начало месяца и для решения финансовых вопросов. Вероятны удачные сделки, а также денежные 
							 поступления из неожиданных источников. Кроме того, есть шанс, что вам вернут старые долги, заплатят 
							 за какую-то работу, проделанную раньше.
							 Во второй половине июня полезно будет несколько снизить деловую активность, переключиться на что-то 
							 другое или просто отдохнуть и восстановить силы. Решение некоторых важных для вас вопросов может 
							 откладываться на неопределенные срок, это заставит волноваться. Однако серьезных причин для 
							 переживаний нет, все сложится удачным для вас образом.
							 Важными станут отношения с близкими. Старайтесь больше времени проводить с теми, кто вам дорог, 
							 участвовать в семейных делах, не оставаться в стороне от каких-то домашних проблем, если они возникнут.''')

		if call.data == '4':
			img = open('images2.jpg', 'rb')
			bot.send_photo(chat_id=call.message.chat.id, photo=img)

			bot.send_message(chat_id=call.message.chat.id,
							 text='''Гороскоп на месяц: Рак: В начале июня вам наверняка пригодятся изобретательность и находчивость. 
							 Могут возникать трудности, справиться с которыми вы сможете, действуя по-своему, а не прислушиваясь к чужим 
							 советам. Не исключено, что придется пойти на риск, интуиция подскажет, стоит ли это делать.
							 Ярко будут проявляться ваши лидерские качества, и это будет особенно заметно в профессиональной сфере. 
							 Будет шанс подняться по карьерной лестнице. Некоторым Ракам предложат именно ту работу, о которой вы 
							 давно мечтали. Первая половина месяца также будет удачной для тех, кто учится, занимается исследованиями 
							 или экспериментами.
							 Во второй половине июня нужно будет действовать осторожнее. Стоит обращать больше внимания на мелкие детали, 
							 особенно если вы заключаете сделки, совершаете какие-то крупные покупки. Лучше избегать любой сомнительной 
							 коммерческой деятельности.
							 С точки зрения личных отношений конец месяца будет благоприятным. Вы разберетесь в собственных чувствах и 
							 станете лучше понимать близких, помиритесь с теми, с кем были в ссоре.''')

		if call.data == '5':
			img = open('images3.jpg', 'rb')
			bot.send_photo(chat_id=call.message.chat.id, photo=img)

			bot.send_message(chat_id=call.message.chat.id,
							 text='''Гороскоп на месяц: Лев: В июне полезно будет сосредоточиться на масштабных планах, достижении 
							 долгосрочных целей. У вас будет возможность позаботиться о собственном будущем, подготовиться к 
							 осуществлению каких-то важных проектов. Вероятны полезные знакомства. Многие Львы именно в июне 
							 встретят людей, с которыми будут тесно сотрудничать с течение нескольких ближайших лет.
							 Вероятны перемены в отношениях с близкими. Удастся положить конец конфликтам и недопониманию, 
							 договориться об общих планах и тех делах, которые важны для всех. Первая половина июня будет 
							 благоприятной для семейного отдыха, путешествий с друзьями и родственниками. Позже нужно будет 
							 заняться обустройством дома, сделать какие-то крупные покупки, а также решить вопросы, касающиеся семейного имущества.
							 Июнь будет благоприятным с точки зрения финансов. Ваши доходы могут заметно возрасти. Не исключено, 
							 что вы станете больше работать и будете этому очень рады.''')

		if call.data == '6':
			img = open('download4.jpg', 'rb')
			bot.send_photo(chat_id=call.message.chat.id, photo=img)

			bot.send_message(chat_id=call.message.chat.id,
							 text='''Гороскоп на месяц: Дева: Серьезный подход к делам позволит вам добиться успеха в начале июня. 
							 Едва ли это будет даваться легко: потрудиться придется, не все будет складываться именно так, как вам 
							 хотелось бы. Не исключено, что нужно будет искать новых помощников и союзников, поскольку люди, на которых 
							 вы прежде полагались, не смогут вас поддержать.
							 Вы справитесь с трудностями благодаря своему опыту и интуиции, подсказки которой всегда будут точными. 
							 Окружающие будут охотно давать советы, но вы поймете: не стоит прислушиваться ко всему.
							 Вторая половина июня пройдет спокойнее. Будет возможность отвлечься от дел, вспомнить о собственных 
							 интересах, не связанных с работой. Найдется время и для нового хобби, благодаря которому вы познакомитесь 
							 с очень интересными людьми. Не исключено начало романтических историй или восстановление отношений, которыми 
							 вы прежде дорожили.
							 У вас могут появиться идеи, которые покажутся окружающими странными, далекими от реальности. Возможно, 
							 задуманное действительно не удастся сразу воплотить в жизнь, но позже вы обязательно вернетесь к этим планам.''')

		if call.data == '7':
			img = open('download5.jpg', 'rb')
			bot.send_photo(chat_id=call.message.chat.id, photo=img)

			bot.send_message(chat_id=call.message.chat.id,
							 text='''Гороскоп на месяц: Весы: В начале июня вы проявите завидную настойчивость и сделаете то, что прежде 
							 казалось почти невозможным. Это время хорошо подойдет для того, чтобы проявить инициативу в работе. Ваши 
							 идеи заинтересуют людей, от которых многое зависит. Не исключено, что вы найдете влиятельных союзников и 
							 при их поддержек осуществите то, что задумали давным-давно.
							 Важно не торопиться. Помните: сейчас вы работаете на будущее, поэтому лучше не рассчитывать на скорые победы, 
							 немедленные результаты.
							 Позже наступит благоприятное время для решения организационных вопросов, обращения в государственные 
							 организации, оформления документов. Не возникнет каких-то бюрократических проблем, все нужные люди окажутся 
							 на месте, важные бумаги вовремя окажутся у вас.
							 С точки зрения личных отношений вторая половина июня будет благоприятнее первой. Проблемы, тревожившие 
							 вас раньше, решатся, и ничто не будет омрачать общения с людьми, которые вам дороги''')

		if call.data == '8':
			img = open('download6.jpg', 'rb')
			bot.send_photo(chat_id=call.message.chat.id, photo=img)

			bot.send_message(chat_id=call.message.chat.id,
							 text='''Гороскоп на месяц: Скорпион: В начале июня вам стоит особенно внимательно следить за своим 
							 эмоциональным состоянием, не переутомляться и избегать стрессовых ситуаций. Возникающие проблемы и 
							 трудности могут казаться вам значительными, хотя в другое время вы легко справились бы с ними. 
							 Рядом будут люди, способные и подбодрить вас, и оказать реальную помощь. Не стесняйтесь обращаться за 
							 поддержкой к тем, кому доверяете.
							 С точки зрения работы этот период будет не самым простым: вероятны задержки в делах, могут нарушаться 
							 старые договоренности. Но вы не станете сидеть сложа руки, предпримете верные шаги и вовремя добьетесь 
							 всех поставленных целей.
							 Вторая половина июня будет и более плодотворной, и более простой. Поддержка звезд будет заметной во 
							 всех сферах жизни, вы почувствуете, что обстоятельства складываются исключительно удачно. Это время 
							 хорошо подойдет для того, чтобы проявлять инициативу, браться за что-то новое, экспериментировать. 
							 Не бойтесь поступать по-своему: вам многое будет даваться легко.''')

		if call.data == '9':
			img = open('images4.jpg', 'rb')
			bot.send_photo(chat_id=call.message.chat.id, photo=img)

			bot.send_message(chat_id=call.message.chat.id,
							 text='''Гороскоп на месяц: Стрелец: В начале июня вы сможете добиться заметных успехов в делах благодаря 
							 своему обаянию и умению ладить с людьми. Это время будет очень благоприятным для общения и новых знакомств. 
							 Вы найдете новых союзников и вскоре подружитесь с ними. Не исключено и начало романтических отношений. Они 
							 будут развиваться стремительно, и вас это порадует.
							 Можно вернуться к каким-то старым идеям и проектам: не исключено, что сейчас вы сможете воплотить в жизнь 
							 задуманное раньше. Решатся проблемы, о которых вы в последнее время много размышляли. Станет ясно, что 
							 теперь можно взяться за что-то совершенно новое. А интуиция подскажет, на чем именно стоит сосредоточиться.
							 Позже могут произойти какие-то неожиданные события, из-за которых вам нужно будет изменить планы. Не 
							 исключены задержки в делах, рабочие проблемы. Это заставит поволноваться, но вскоре выясниться, что все 
							 возникшие трудности не так уж серьезны, с ними можно быстро справиться.
							 Последние дни июня порадуют. В это время возможны какие-то удачные совпадения и хорошие новости, 
							 предложения, на которые вы без долгих раздумий ответите согласием.''')

		if call.data == '10':
			img = open('download7.jpg', 'rb')
			bot.send_photo(chat_id=call.message.chat.id,photo=img)

			bot.send_message(chat_id=call.message.chat.id,
							 text='''Гороскоп на месяц: Козерог: Старайтесь спокойно и конструктивно подходить к решению любых 
							 вопросов, возникающих в начале июня. Это не самое простое время, но непреодолимых преград на пути не 
							 возникнет. Придется заниматься несколькими делами сразу, и тут важными окажутся серьезный подход и 
							 самодисциплина. Важно ничего не пускать на самотек, особенно в сфере работы и бизнеса. Уделяйте внимание 
							 даже самым мелким деталям, старайтесь замечать то, что другим показалось незначительным.
							 Важным будет общение с близкими. Они поддержат вас и дадут отличные советы, да и просто выслушают, 
							 когда это потребуется. Будет возможность съездить куда-то вместе с друзьями или родственниками, и даже 
							 небольшое путешествие всем подарит массу позитивных эмоций.
							 Вторая половина июня – время спокойной плодотворной работы, решения серьезных задач. Благоприятным 
							 будет оно и для учебы, повышения квалификации. Вы получите полезную информацию, узнаете много 
							 интересного. Некоторые Козероги к тому же обзаведутся полезными связями.
							 Этот период будет благоприятным для покупок и сделок: деловое чутье не подведет вас, поможет принять верное решение.''')

		if call.data == '11':
			img = open('download8.jpg', 'rb')
			bot.send_photo(chat_id=call.message.chat.id, photo=img)

			bot.send_message(chat_id=call.message.chat.id,
							 text='''Гороскоп на месяц: Водолей: Будет много интересного. Июнь может принести большие перемены во 
							 всех сферах жизни, и хорошо, если вы воспримете их с радостью и энтузиазмом, не станете цепляться за 
							 старое и привычное. Некоторым Водолеям предстоит принять непростые решения. Они сделают это самостоятельно, 
							 ни с кем не советуясь, – и не пожалеют.
							 Не всегда просто будут складываться деловые отношения. Порой вам будет непросто держать свои эмоции под 
							 контролем, сохранять самообладание. Тут выручит опыт. Вспоминайте о тех трудностях, которые вы преодолели 
							 раньше, о своих победах – все это поможет не поддаться на провокации, взять ситуацию под контроль.
							 Общаться с близкими будет куда проще и приятнее. Вы получите поддержку, в которой будете нуждаться, 
							 увидите, что вас действительно хорошо понимают. Если в последнее время возникали какие-то разногласия, 
							 сейчас их удастся преодолеть.
							 С точки зрения финансов июнь будет достаточно благоприятным. Едва ли вы мгновенно разбогатеете, но 
							 удачные сделки вполне можете заключить. А вот серьезные расходы маловероятны.''')

		if call.data == '12':
			img = open('images.jpg', 'rb')
			bot.send_photo(chat_id=call.message.chat.id, photo=img)

			bot.send_message(chat_id=call.message.chat.id,
							 text='''Гороскоп на месяц: Рыбы: Начало июня будет полным интересных и вдохновляющих событий. 
							 Появятся интересные идеи, новые планы. Окружающие могут сомневаться в том, что вы сможете воплотить 
							 задуманное в жизнь, но вы ни на минуту не утратите уверенности в успехе. Благодаря подсказкам интуиции 
							 вы найдете ответы на многие вопросы, справитесь с тем, что не получилось у других.
							 Повезет тем, кто в первой половине июня возьмется за что-то новое. Такие Рыбы быстро поймут, как 
							 надо действовать, и без труда найдут людей, к которым можно обратиться за помощью и советом. Это 
							 время будет благоприятным для начала сотрудничества. Новые партнеры вскоре станут вашими друзьями.
							 Вторая половина месяца будет благоприятной для встреч и переговоров, общения с людьми, которых вы 
							 хотели бы видеть своими союзниками. Удастся произвести на них хорошее впечатление.
							 Кроме того, данный период хорошо подойдет для завершения старых дел, решения вопросов, над которыми 
							 вы в последнее время много размышляли. Из нескольких возможных вариантов вы выберете лучший.''')

if __name__ == "__main__":
	bot.polling(none_stop=True)
# bot.polling()


# keyboard.row(aries, taurus, gemini, cancer)
# keyboard.row(leo, virgo, libra, scorpio)
# keyboard.row(sagittarius, capricorn, aquarius, pisces)
# keyboard.insert(pisces)
# 	return keyboard()