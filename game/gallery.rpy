
########################################################################################################################
#### CG GALLERY #######################################################################################################
########################################################################################################################
init python:
    # size of thumbnails in gallery
    thumbnail_x = 270
    thumbnail_y = 152


    # gallery of prologue images
    gallery_cg_items = ["cg1", "cg2", "cg3", "cg4", "cg5", "cg6", "cg7","cg8", "cg9", "cg10", "cg11", "cg12", "cg13", "cg14", "cg15", "cg16", "cg17", "cg18", 'cg19',
    'cg20', 'cg21', 'cg22', 'cg23', 'cg24', 'cg25', 'cg26', 'cg27', 'cg28', 'cg29', 'cg30', 'cg31', 'cg32', 'cg33', 'cg34', 'cg35', 'cg36', 'cg37', 'cg38', 'cg39', 
    'cg40', 'cg41', 'cg64', 'cg65', 'cg66', 'cg42', 'cg43', 'cg44', 'cg45', 'cg46', 'cg47', 'cg48', 'cg49', 'cg56', 'cg57', 'cg58', 'cg106', 'cg50', 'cg215', 'cg216', 'cg123', 'cg51', 'cg52', 'cg53', 'cg107', 'cg310', 'cg59', 'cg60', 
    'cg61', 'cg54', 'cg55', 'cg119', 'cg120', 'cg129', 'cg130', 'cg62', 'cg63', 'cg466', 'cg67', 'cg231', 'cg459', 'cg460', 'cg461', 'cg462', 'cg463', 'cg464', 'cg465', 'cg188', 'cg124', 'cg68', 'cg311', 'cg94', 'cg95', 'cg127', 'cg128',  'cg69', 'cg89', 'cg90', 'cg91',  'cg195', 'cg196', 'cg197', 'cg198', 'cg199',
    'cg233', 'cg72', 'cg73', 'cg74', 'cg75', 'cg105', 'cg76', 'cg77', 'cg78', 'cg79', 'cg443', 'cg108', 'cg109', 'cg186', 'cg187', 'cg80', 'cg81', 'cg82', 'cg349', 'cg184', 'cg185', 'cg202', 'cg83', 'cg84', 'cg85', 'cg86', 'cg87',
    'cg88', 'cg98', 'cg97', 'cg96', 'cg92', 'cg93', 'cg117', 'cg118', 'cg313', 'cg99', 'cg100', 'cg101', 'cg147', 'cg148', 'cg149', 'cg359', 'cg360', 'cg361', 'cg362', 'cg102', 'cg103', 'cg104', 'cg321', 'cg189', 'cg110', 'cg111', 'cg112', 'cg113', 'cg114',
    'cg115', 'cg116', 'cg121', 'cg122', 'cg136', 'cg125', 'cg126', 'cg414', 'cg131', 'cg132', 'cg133', 'cg140', 'cg363', 'cg364', 'cg134', 'cg135', 'cg305', 'cg137', 'cg138', 'cg139', 'cg141', 'cg142', 'cg143', 'cg144', 'cg145', 'cg146', 'cg150', 'cg151',
    'cg152', 'cg153', 'cg163', 'cg154', 'cg155', 'cg156', 'cg157', 'cg164', 'cg158', 'cg159', 'cg160', 'cg161', 'cg162', 'cg165','cg166', 'cg167', 'cg168', 'cg169', 'cg170', 'cg175', 'cg176', 'cg177', 
    'cg178', 'cg179', 'cg180', 'cg206', 'cg207', 'cg208', 'cg209' , 'cg210', 'cg211', 'cg190', 'cg191', 'cg192', 'cg193', 'cg194', 'cg171', 'cg172', 'cg173', 'cg306', 'cg181', 'cg182', 'cg183', 'cg174', 'cg217', 'cg218', 'cg200', 'cg201', 'cg212', 'cg203', 'cg204', 'cg205',
    'cg213', 'cg227', 'cg382', 'cg383', 'cg384', 'cg385', 'cg386', 'cg387', 'cg287', 'cg369', 'cg228', 'cg229', 'cg230', 'cg225', 'cg226', 'cg219', 'cg220', 'cg221', 'cg222', 'cg223', 'cg224', 'cg232', 'cg234', 'cg235', 'cg236', 'cg237', 'cg238', 'cg239', 'cg240', 'cg241', 'cg413', 'cg242', 'cg243', 'cg374', 'cg375', 'cg378', 'cg379', 'cg380', 'cg244',
    'cg245', 'cg246', 'cg247', 'cg248', 'cg249', 'cg438', 'cg437', 'cg250', 'cg251', 'cg252', 'cg253', 'cg254', 'cg255', 'cg358', 'cg256', 'cg257', 'cg258', 'cg259', 'cg260', 'cg261','cg262', 'cg263', 'cg264', 'cg388', 'cg389', 'cg265', 'cg266', 'cg267', 'cg268', 'cg269', 'cg270', 'cg312',
    'cg271', 'cg272', 'cg273', 'cg274', 'cg275', 'cg276', 'cg277', 'cg278', 'cg279', 'cg280', 'cg281', 'cg315', 'cg282', 'cg283', 'cg284', 'cg285', 'cg286', 'cg288', 'cg289', 'cg290', 'cg291', 'cg292', 'cg293', 'cg294', 'cg295', 'cg296', 
    'cg297', 'cg298', 'cg299', 'cg300', 'cg301', 'cg302', 'cg304', 'cg303', 'cg307', 'cg308', 'cg314', 'cg316', 'cg317', 'cg318', 'cg319', 'cg320', 'cg350', 'cg351', 'cg352', 'cg353', 'cg322', 'cg323', 'cg381', 'cg324', 'cg325', 'cg326', 'cg327', 'cg328', 'cg329', 'cg330',
    'cg331', 'cg332', 'cg333', 'cg334', 'cg335', 'cg336', 'cg337', 'cg338', 'cg339', 'cg340', 'cg341', 'cg342', 'cg343', 'cg344', 'cg345', 'cg346', 'cg347', 'cg348', 'cg354', 'cg355', 'cg356', 'cg357', 'cg365', 'cg366', 'cg367', 'cg368',
    'cg370', 'cg371', 'cg372', 'cg373', 'cg214', 'cg444', 'cg390', 'cg391', 'cg392', 'cg393', 'cg394', 'cg395', 'cg412', 'cg396', 'cg397', 'cg398', 'cg399', 'cg400', 'cg432', 'cg433', 'cg434', 'cg435', 'cg436', 'cg401', 'cg402', 'cg403', 'cg404', 'cg405', 'cg406', 'cg407', 'cg408', 'cg409',
    'cg410', 'cg411', 'cg415', 'cg416', 'cg417', 'cg418', 'cg419', 'cg420', 'cg421', 'cg422', 'cg423', 'cg424', 'cg425', 'cg426', 'cg427', 'cg428', 'cg429', 'cg430', 'cg431', 'cg439', 'cg440', 'cg441', 'cg442', 'cg445', 'cg446', 'cg447', 'cg448', 'cg449', 'cg450', 'cg451', 'cg452', 'cg453', 'cg454', 'cg455', 'cg456', 'cg457', 'cg458',
    'cg467', 'cg468', 'cg469', 'cg470', 'cg471', 'cg472', 'cg473', 'cg474', 'cg475', 'cg476', 'cg477', 'cg478', 'cg479', 'cg480', 'cg481', 'cg482', 'cg483', 'clihj3', 'clihj8', 'cg484', 'cg484', 'cg491', 'cg492', 'cg493', 'cg494', 'cg495', 'cg496', 'cg497', 'cg498', 'cg499', 'cg500',
    'cg501', 'cg502', 'cg503', 'cg504', 'cg505', 'cg512', 'cg513', 'cg514', 'cg515', 'cg516', 'cg517', 'cg518', 'cg519', 'cg520', 'cg521', 'cg526', 'cg527', 'cg528', 'cg529', 'cg530', 'cg535', 'cg536', 'cg537', 'cg542', 'cg543', 'cg544', 'cg545', 'cg546', 'cg547', 'cg548', 'cg549', 'cg550',
    'cg551', 'cg552', 'cg553', 'cg554', 'cg555', 'cg556', 'cg557', 'cg558', 'cg559', 'cg560', 'cg561', 'cg562', 'cg563', 'cg564', 'cg565', 'cg566', 'cg567', 'cg568', 'cg569', 'cg570', 'cg571', 'cg572', 'cg573', 'cg574', 'cg575', 'cg576', 'cg577', 'cg578', 'cg579', 'cg580', 'cg581', 'cg582',
    'cg583', 'cg584', 'cg585','cg586', 'cg587', 'cg588', 'cg589', 'cg590', 'cg591', 'cg592', 'cg593', 'cg594', 'cg595', 'cg607', 'cg596', 'cg597', 'cg598', 'cg599', 'cg601', 'cg602', 'cg603', 'cg604', 'cg608', 'cg618', 'cg619', 'cg620', 'cg630', 'cg638', 'cg639',
    'cg605', 'cg606', 'cg609', 'cg610', 'cg611', 'cg612', 'cg613', 'cg614', 'cg615', 'cg616', 'cg617', 'cg600', 'cg657', 'cg658', 'cg659', 'cg660', 'cg661', 'cg665', 'cg666', 'cg667', 'cg668', 'cg669', 'cg670', 'cg671', 'cg675', 'cg676', 'cg677', 'cg678', 'cg679',
    'cg680', 'cg681', 'cg682', 'cg700', 'cg701', 'cg702', 'cg703', 'cg704', 'cg705', 'cg706', 'cg716', 'cg717', 'cg718', 'cg719', 'cg720', 'cg721', 'cg722', 'cg723', 'cg724', 'cg725', 'cg726', 'cg727', 'cg728', 'cg729', 'cg730', 'cg731', 'cg732', 'cg733',
    'cg734', 'cg735', 'cg736', 'cg737', 'cg738', 'cg739', 'cg740', 'cg741', 'cg742', 'cg743', 'cg744', 'cg745', 'cg746', 'cg747', 'cg764', 'cg765', 'cg766', 'cg767', 'cg768', 'cg769', 'cg770', 'cg771', 'cg785', 'cg786', 'cg787', 'cg788', 'cg789', 'cg790', 'cg791', 'cg792', 'cg793',
    'cg794', 'cg795', 'cg796', 'cg797', 'cg798', 'cg799', 'cg800', 'cg801', 'cg802', 'cg803', 'cg804', 'cg805', 'cg806', 'cg807', 'cg809', 'cg810', 'cg811', 'cg812', 'cg813', 'cg814', 'cg815', 'cg816', 'cg817', 'cg818', 'cg819', 'cg820', 'cg821', 'cg822', 'cg823', 'cg824', 'cg825',
    'cg826', 'cg827', 'cg828', 'cg829', 'cg830', 'cg847', 'cg848', 'cg849', 'cg850', 'cg851', 'cg852', 'cg853', 'cg854', 'cg855', 'cg856', 'cg857', 'cg858', 'cg859', 'cg860', 'cg861', 'cg862', 'cg863', 'cg864', 'cg865', 'cg866', 'cg867', 'cg868', 'cg869', 'cg870',
    'cg871', 'cg872', 'cg873', 'cg874', 'cg875', 'cg876', 'cg877', 'cg878', 'cg879', 'cg880', 'cg881', 'cg882', 'cg883', 'cg884', 'cg885', 'cg886', 'cg887', 'cg888', 'cg889', 'cg890', 'cg891', 'cg892', 'cg893', 'cg894', 'cg895', 'cg896', 'cg897', 'cg898', 'cg899',
    'cg900', 'cg901', 'cg902', 'cg903', 'cg904', 'cg905', 'cg906', 'cg907', 'cg908', 'cg909', 'cg910', 'cg911', 'cg912', 'cg913', 'cg914', 'cg915', 'cg916', 'cg917', 'cg918', 'cg919', 'cg920', 'cg921', 'cg922', 'cg923', 'cg924', 'cg925', 'cg926', 'cg927', 'cg928',
    'cg929', 'cg930', 'cg931', 'cg932', 'cg933', 'cg934', 'cg935', 'cg936', 'cg937', 'cg938', 'cg939', 'cg940', 'cg941', 'cg942', 'cg943', 'cg944', 'cg945', 'cg946', 'cg947', 'cg948', 'cg949', 'cg950', 'cg951', 'cg942', 'cg953', 'cg954', 'cg955', 'cg956', 'cg957', 
    'cg958', 'cg959', 'cg960', 'cg961', 'cg962', 'cg963', 'cg964', 'cg965', 'cg966', 'cg967', 'cg968', 'cg969', 'cg970', 'cg971', 'cg972', 'cg973', 'cg974', 'cg975', 'cg976']
   
   
    regular_gallery = Gallery()
    for gal_item in gallery_cg_items:
        regular_gallery.button(gal_item + " butt")
        regular_gallery.unlock_image(gal_item)
    regular_gallery.transition = dissolve


    # gallery of training images
    training_cg_items = ['alexia_maid_1', 'dummy', 'dummy', 'alexia_library_1']
    training_gallery = Gallery()
    for gal_item in training_cg_items:
        training_gallery.button(gal_item + " butt")
        training_gallery.unlock_image(gal_item)
    training_gallery.transition = dissolve


    # info for some cg gallery images: {gallery_image: (image_name, artist, website or None), ...}
    artists_info = {
    'cg1': ('Afternoon Delight 1', 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg2': ('Afternoon Delight 2', 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg3': ('Afternoon Delight 3', 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg4': ('Afternoon Delight 4', 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg5': ('A Stranger Arrives', 'HikariYumiya', 'http://hikariyumiya.deviantart.com/'),
    'cg6': ('Blackholt Ambush', 'HikariYumiya', 'http://hikariyumiya.deviantart.com/'),
    'cg7': ('The Demon Revealed', 'HikariYumiya', 'http://hikariyumiya.deviantart.com/'),
    'cg8': ('Smoke and Flame', 'HikariYumiya', 'http://hikariyumiya.deviantart.com/'),
    'cg9': ('Rowan Bowed', 'HikariYumiya', 'http://hikariyumiya.deviantart.com/'),
    'cg10': ('Before the Gates', 'HikariYumiya', 'http://hikariyumiya.deviantart.com/'),
    'cg11': ('Slave to Jezera 1 ', 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg12': ('Slave to Jezera 2', 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg13': ('Slave to Jezera 3', 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg14': ('Slave to Jezera 4', 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg15': ('Taken by the Demon 1', 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg16': ('Taken by the Demon 2', 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg17': ('Taken by the Demon 3', 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg18': ('Taken by the Demon 4', 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg19': ('Reunion', 'HikariYumiya', 'http://hikariyumiya.deviantart.com/'),
    'cg20': ("The Demon's Kiss 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg21': ("The Demon's Kiss 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg22': ("The Demon's Kiss 3", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg23': ("Andras' Anal Assault 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg24': ("Andras' Anal Assault 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg25': ("Andras' Anal Assault 3", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg26': ("Andras' Anal Assault 4", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg27': ("Face Down, Ass Up 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg28': ("Face Down, Ass Up 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg29': ("Face Down, Ass Up 3", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg30': ("To Sleep, Perchance 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg31': ("To Sleep, Perchance 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg32': ("To Sleep, Perchance 3", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg33': ("Lovers Reunited 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg34': ("Lovers Reunited 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg35': ("Puppets on a String 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg36': ("Puppets on a String 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg37': ("Puppets on a String 3", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg38': ("Puppets on a String 4", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg39': ("Puppets on a String 5", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg40': ("Puppets on a String 6", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg41': ("Puppets on a String 7", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg42': ("Putting on a Show 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg43': ("Putting on a Show 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg44': ("Putting on a Show 3", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg45': ("Putting on a Show 4", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg46': ("Putting on a Show 5", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg47': ("Putting on a Show 6", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg48': ("Putting on a Show 7", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg49': ("Putting on a Show 8", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg50': ("Wine her, Dine her... 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg51': ("Size Counts 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg52': ("Size Counts 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg53': ("Size Counts 3", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg54': ("It's Easy Being Green 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg55': ("It's Easy Being Green 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg56': ("Putting on a Show 9", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg57': ("Putting on a Show 10", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg58': ("Putting on a Show 11", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg59': ("Keep-ing it Real 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg60': ("Keep-ing it Real 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg61': ("Keep-ing it Real 3", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg62': ("On the Leash 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg63': ("On the Leash 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg64': ("Puppets on a String 8", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg65': ("Puppets on a String 9", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg66': ("Puppets on a String 10", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg67': ("Table Manners 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg68': ("Friends Reunited 3", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg69': ("The Goblin's Bargain 3", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg72': ("Delf Dipping 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg73': ("Delf Dipping 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg74': ("Delf Dipping 3", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg75': ("Delf Dipping 4", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg76': ("One Drink Too Many 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg77': ("One Drink Too Many 3", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg78': ("One Drink Too Many 4", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg79': ("One Drink Too Many 5", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg80': ("Cliohna's Experiment 3", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg81': ("Village Threesome 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg82': ("Village Threesome 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg83': ("Married Love 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg84': ("Married Love 3", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg85': ("Devil's Bargain 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg86': ("Devil's Bargain 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg87': ("Devil's Bargain 3", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg88': ("Devil's Bargain 4", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg89': ("Cla-Bow's Proposition 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg90': ("Cla-Bow's Proposition 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg91': ("Cla-Bow's Proposition 3", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg92': ("Jezera's Task 4", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg93': ("Jezera's Task 5", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg94': ("Under the Table 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg95': ("Under The Table 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg96': ("Jezera's Task 3", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg97': ("Jezera's Task 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg98': ("Jezera's Task 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg99': ("Alexia's New Toy 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg100': ("Alexia's New Toy 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg101': ("Alexia's New Toy 3", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg102': ("Dinner is Served 5", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg103': ("Dinner is Served 6", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg104': ("Dinner is Served 7", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg105': ("One Drink Too Many 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg106': ("Wine her, Dine her... 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg107': ("The Wounded Beast", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg108': ("Minotaur Hospitality 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg109': ("Minotaur Hospitality 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg110': ("Rowan's Reward 3", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg111': ("Rowan's Reward 4", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg112': ("The Knight's Delight 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg113': ("The Knight's Delight 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg114': ("The Knight's Delight 3", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg115': ("Finger Lickin' Good 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg116': ("Finger Lickin' Good 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg117': ("Double Trouble 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg118': ("Double Trouble 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg119': ("Subordinate Blowbang 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg120': ("Subordinate Blowbang 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg121': ("The Web of the Spider 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg122': ("The Web of the Spider 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg123': ("An Audience with Andras", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg124': ("Friends Reunited 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg125': ("Helyana's Hunger 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg126': ("Helayna's Hunger 3", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg127': ("The Goblin's Bargain 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg128': ("The Goblin's Bargain 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg129': ("A Trip to the Arena 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg130': ("a Trip to the Arena 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg131': ("Don't Tease the Animals 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg132': ("Don't Tease the Animals 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg133': ("Don't Tease the Animals 3", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg134': ("Screwing the Help 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg135': ("Screwing the Help 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg136': ("Helyana's Hunger 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg137': ("The Witch's Thrall 1", 'Lewd Brush', ''),
    'cg138': ("The Witch's Thrall 2", 'Lewd Brush', ''),
    'cg139': ("The Witch's Thrall 3", 'Lewd Brush', ''),
    'cg140': ("Kissing the Help", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg141': ("The Hunter's Trap 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg142': ("The Hunter's Trap 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg143': ("The Wisp's Tithe 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg144': ("The Wisp's Tithe 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg145': ("The Wisp's Tithe 3", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg146': ("The Wisp's Tithe 4", 'momdadno', 'http://momdadno.tumblr.com/'),    
    'cg147': ("Airtight 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg148': ("Airtight 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg149': ("Airtight 3", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg150': ("Perks of the Job 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg151': ("Perks of the Job 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg152': ("Perks of the Job 3", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg153': ("Punishing the Help 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg154': ("Three's Company 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg155': ("Three's Company 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg156': ("Three's Company 3", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg157': ("Three's Company 4", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg158': ("Fun with Wulumps 1", 'Lewd Brush', ''),
    'cg159': ("Fun with Wulumps 2", 'Lewd Brush', ''),
    'cg160': ("Fun with Wulumps 3", 'Lewd Brush', ''),
    'cg161': ("Fun with Wulumps 4", 'Lewd Brush', ''),
    'cg162': ("Fun with Wulumps 5", 'Lewd Brush', ''),
    'cg163': ("Punishing the Help 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg164': ("Three's Company 5", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg165': ("Fun with Wulumps 6", 'Lewd Brush', ''),
    'cg166': ("Fun with Wulumps 7", 'Lewd Brush', ''),
    'cg167': ("Fun with Wulumps 8", 'Lewd Brush', ''),
    'cg168': ("Fun with Wulumps 9", 'Lewd Brush', ''),
    'cg169': ("Fun with Wulumps 10", 'Lewd Brush', ''),
    'cg170': ("Fun with Wulumps 11", 'Lewd Brush', ''),
    'cg171': ("Helayna's Daydream 1", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg172': ("Helayna's Daydream 2", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg173': ("Helayna's Daydream 3", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg174': ("Indarah Gets the D 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg175': ("Fun with Wulumps 12", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg176': ("Fun with Wulumps 13", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg177': ("Fun with Wulumps 14", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg178': ("Fun with Wulumps 15", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg179': ("Fun with Wulumps 16", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg180': ("Fun with Wulumps 17", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg181': ("Helayna's Daydream 5", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg182': ("Helayna's Daydream 6", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg183': ("Helayna's Daydream 7", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg184': ("Village Threesome 4", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg185': ("Village Threesome 5", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg186': ("Cliohna's Experiment 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg187': ("Cliohna's Experiment 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg188': ("Friends Reunited 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg189': ("Rowan's Reward 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg190': ("The Demon in the Dungeon 7", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg191': ("The Demon in the Dungeon 8", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg192': ("The Demon in the Dungeon 9", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg193': ("The Demon in the Dungeon 10", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg194': ("The Demon in the Dungeon 11", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg195': ("Goblin Paizuri 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg196': ("Goblin Paizuri 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg197': ("Goblin Paizuri 3", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg198': ("Goblin Paizuri 4", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg199': ("Goblin Paizuri 5", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg200': ("The Anal Adventurer 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg201': ("Draining Dazzanath 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg202': ("Married Love 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg203': ("At Her Mistresses' Feet 1", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg204': ("At Her Mistresses' Feet 2", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg205': ("At Her Mistresses Feet' 3", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg206': ("The Demon in the Dungeon 1", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg207': ("The Demon in the Dungeon 2", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg208': ("The Demon in the Dungeon 3", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg209': ("The Demon in the Dungeon 4", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg210': ("The Demon in the Dungeon 5", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg211': ("The Demon in the Dungeon 6", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg212': ("Draining Dazzanath 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg213': ("Secretarial Duties 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg214': ("Under Jezera's Thrall 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg215': ("Preparing the Master 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg216': ("Preparing the Master 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg217': ("Indarah Gets the D 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg218': ("Indarah Gets the D 3", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg219': ("Shaya's Dance 1", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg220': ("Shaya's Dance 2", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg221': ("Shaya's Dance 3", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg222': ("Shaya's Dance 4", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg223': ("Shaya's Dance 5", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg224': ("Shaya's Dance 6", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg225': ("The Broken Noble 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg226': ("The Broken Noble 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg227': ("The Warlord's Slave 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg228': ("Hero Spitroast 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg229': ("Hero Spitroast 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg230': ("Hero Spitroast 3", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg231': ("Table Manners 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg232': ("An Orcish Reward 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg233': ("Draith's Reward 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg234': ("A Sinful Night With Emma 1", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg235': ("A Sinful Night With Emma 2", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg236': ("A Sinful Night With Emma 3", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg237': ("A Sinful Night With Emma 4", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg238': ("A Pure Night With Emma 1", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg239': ("A Pure Night With Emma 2", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg240': ("A Pure Night With Emma 3", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg241': ("A Pure Night With Emma 4", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg242': ("An Elfish Threesome 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg243': ("An Elfish Threesome 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg244': ("The Beast of War 1", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg245': ("The Beast of War 2", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg246': ("The Beast of War 3", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg247': ("The Beast of War 4", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg248': ("The Beast of War 5", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg249': ("Demonic Deception 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg250': ("The Prince of Tomes 1", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg251': ("The Prince of Tomes 2", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg252': ("The Prince of Tomes 3", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg253': ("Delane's Bad End", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg254': ("A Bedslave's Reward 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg255': ("A Bedslave's Reward 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg256': ("Draith's Punishment 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg257': ("Draith's Punishment 3", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg258': ("Draith's Punishment 4", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg259': ("Jezera's Dungeon Desires 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg260': ("Jezera's Dungeon Desires 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg261': ("Jezera's Dungeon Desires 3", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg262': ("Castle Bloodmeen", 'Jorge Jacinto', 'https://www.deviantart.com/jjcanvas/'),
    'cg263': ("Drider Exhibitionist 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg264': ("Drider Exhibitionist 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg265': ("Doran Learns His Place 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg266': ("Helayna the Cuckquean 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg267': ("Master Fluffer 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg268': ("Master Fluffer 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg269': ("Master Fluffer 3", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg270': ("Master Fluffer 4", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg271': ("Love in the Woods 1", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg272': ("Love in the Woods 2", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg273': ("Love in the Woods 3", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg274': ("Love in the Woods 4", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg275': ("Love in the Woods 5", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg276': ("Love in the Woods 6", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg277': ("Love in the Woods 7", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg278': ("Andras the Patron 1", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg279': ("Andras the Patron 2", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg280': ("Andras the Patron 3", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg281': ("Andras the Patron 4", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg282': ("Riding the Bull 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg283': ("Riding the Bull 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg284': ("Alexia's Surprise 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg285': ("Alexia's Surprise 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg286': ("Wife Takes it Deep 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg287': ("Hungry for Two Dicks 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg288': ("Jezera's Bovine Toy 1", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg289': ("Jezera's Bovine Toy 2", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg290': ("Jezera's Bovine Toy 3", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg291': ("Jezera's Bovine Toy 4", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg292': ("Jezera's Bovine Toy 5", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg293': ("Jezera's Bovine Toy 6", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg294': ("Jezera's Bovine Toy 7", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg295': ("Sex in the Moonlight 1", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg296': ("Sex in the Moonlight 2", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg297': ("Sex in the Moonlight 3", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg298': ("Sex in the Moonlight 4", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg299': ("Sex in the Moonlight 5", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg300': ("Sex in the Moonlight 6", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg301': ("Forbidden Fruit 1", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg302': ("Forbidden Fruit 2", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg303': ("Forbidden Fruit 3", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg304': ("Forbidden Fruit 4", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg305': ("The Midnight Court Approaches", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg306': ("Helayna's Daydream 4", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg307': ("Bathing the Master 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg308': ("Bathing the Master 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg309': ("A Break from the Fighting", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg310': ("The Fallen Knight", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg311': ("The Goblin Dinner 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg312': ("Awkward Silence", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg313': ("Group Hug", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg314': ("The Demon's Demonstration", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg315': ("Tasting the Bull", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg316': ("Tasting the Dragon", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg317': ("Riding the Dragon", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg318': ("Helayna Opens Wide 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg319': ("Helayna Opens Wide 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg320': ("Helayna Opens Wide 3", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg321': ("Rowan's Reward 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg322': ("The Elves' Dark Sacrifice 1", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg323': ("The Elves' Dark Sacrifice 2", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg324': ("The Old Orc's True Love 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg325': ("How Green Was Her Valley 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg326': ("How Green Was Her Valley 2", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg327': ("How Green Was Her Valley 3", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg328': ("How Green Was Her Valley 4", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg329': ("How Green Was Her Valley 5", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg330': ("The Young Aspirant's Training 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg331': ("The Young Aspirant's Training 2", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg332': ("The Young Aspirant's Training 3", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg333': ("The Young Aspirant's Training 4", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg334': ("The Young Aspirant's Training 5", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg335': ("The Young Aspirant's Training 6", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg336': ("The Commander's Interrogation 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg337': ("The Commander's Interrogation 2", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg338': ("The Commander's Interrogation 3", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg339': ("The Commander's Interrogation 4", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg340': ("The Commander's Interrogation 5", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg341': ("Delane's Wild Ride 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg342': ("Delane's Wild Ride 2", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg343': ("Delane's Wild Ride 3", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg344': ("Delane's Wild Ride 4", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg345': ("Delane's Wild Ride 5", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg346': ("Delane's Wild Ride 6", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg347': ("Delane's Wild Ride 7", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg348': ("Delane's Wild Ride 8", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg349': ("Village Threesome 3", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg350': ("Helayna's Submission Training 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg351': ("Helayna's Submission Training 2", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg352': ("Helayna's Submission Training 3", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg353': ("Helayna's Submission Training 4", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg354': ("The Barmaid's Challenge 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg355': ("The Barmaid's Challenge 2", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg356': ("The Barmaid's Challenge 3", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg357': ("The Barmaid's Challenge 4", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg358': ("Draith's Punishment 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg359': ("Dinner is Served 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg360': ("Dinner is Served 2", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg361': ("Dinner is Served 3", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg362': ("Dinner is Served 4", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg363': ("The Modest Elf Maiden 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg364': ("The Modest Elf Maiden 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg365': ("I Kissed a Girl 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg366': ("I Kissed a Girl 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg367': ("I Kissed a Girl 3", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg368': ("I Kissed a Girl 4", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg369': ("Twice as Good 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg370': ("Massaging his Mistress 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg371': ("Massaging his Mistress 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg372': ("Massaging his Mistress 3", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg373': ("Massaging his Mistress 4", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg374': ("An Elfish Threesome 3", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg375': ("An Elfish Threesome 4", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg376': ("An Elfish Threesome 5", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg377': ("An Elfish Threesome 6", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg378': ("An Elfish Threesome 7", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg379': ("An Elfish Threesome 8", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg380': ("An Elfish Threesome 9", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg381': ("The Old Orc's True Love 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg382': ("The Warlord's Slave 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg383': ("The Warlord's Slave 3", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg384': ("The Warlord's Slave 4", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg385': ("The Warlord's Slave 5", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg386': ("The Warlord's Slave 6", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg387': ("The Warlord's Slave 7", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg388': ("Shaving Lord Doran 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg389': ("Shaving Lord Doran 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg390': ("Air On a G-Spot 1", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg391': ("Air On a G-Spot 2", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg392': ("Air On a G-Spot 3", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg393': ("Air On a G-Spot 4", 'momdadno', 'http://momdadno.tumblr.com/'),
    'cg394': ("A Rider for Rastedel 1", 'Sommelier', 'https://twitter.com/_S0my'),
    'cg395': ("A Rider for Rastedel 2", 'Sommelier', 'https://twitter.com/_S0my'),

    
    'alexia_maid_1': ('Alexia Maid 1', 'momdadno', 'http://momdadno.tumblr.com/'),
    'alexia_library_1': ('Alexia Librarian 1', 'momdadno', 'http://momdadno.tumblr.com/'),
    'alexia_pits_1': ('Alexia Breeding Pits 1', 'momdadno', 'http://momdadno.tumblr.com/'),
    'alexia_barmaid_1': ('Alexia Barmaid 1', 'momdadno', 'http://momdadno.tumblr.com/')
    }


    def GenerateNodes(n):
        d = {}
        for i in range(0, n):
            d[i] = False
        return d
    def pass_node(n):
        if n in persistent.progress_node:
            persistent.progress_node[n] = True
    def PercentComplete():
        count = 0
        for i in persistent.progress_node:
            if persistent.progress_node[i]:
                count +=1
        return int( float(count*100) / len(persistent.progress_node) )
    if persistent.progress_node == None:
        persistent.progress_node = GenerateNodes(12)


init +1 python:
    for gal_item in gallery_cg_items + training_cg_items:
        # create thumbnails for every gallery image
        renpy.image(gal_item + " butt", im.Scale(im.Sepia(ImageReference(gal_item)), thumbnail_x, thumbnail_y))


# semitransparent image for artist info button in cg gallery
image info_button_idle = im.MatrixColor('gui/info button.png', im.matrix.opacity(0.5))


# displays a gallery of images
screen cg_gallery(g_cg, cg_seq):
    # g_cg is instance of Gallery, cg_seq is related sequence of images
    default gal_rows = 3
    default gal_cols = 3
    default gal_cells = gal_rows * gal_cols
    default cg_page = 0
    tag menu
    add "gui/gm_back.jpg"
    use bonus_navigation
    vbox:
        add "gui/frame.png"
        xalign 0.05
        yalign 0.5
    frame background None xpos 10:
        grid gal_rows gal_cols:
            xpos 65
            ypos 90
            spacing 10
            $ i = 0
            $ next_cg_page = cg_page + 1
            # using float(gal_cells) so result of division will not be truncated
            if next_cg_page >= len(cg_seq)/float(gal_cells):
                $ next_cg_page = 0
            for gal_item in cg_seq:
                $ i += 1
                if i <= (cg_page+1)*gal_cells and i>cg_page*gal_cells:
                    fixed:
                        xysize (thumbnail_x+8, thumbnail_y+8)
                        add g_cg.make_button(gal_item + " butt", gal_item + " butt", im.Scale("gui/gallocked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=im.Scale("gui/gallery_border.png", thumbnail_x, thumbnail_y, xalign=0.5, yalign=0.5), background=im.Scale("gui/frame2.png", thumbnail_x+8, thumbnail_y+8, align=(0.5, 0.5)))
                        # if image has associated info for artist and unlocked, add a button to show details screen
                        # it seems not very safe, as this checks for full unlock for gallery button, not directly for image; it is ok for buttons with single image
                        if gal_item in artists_info and (g_cg.get_fraction(gal_item + ' butt', '{locked}') == '0'):
                            imagebutton xalign 1.0 xoffset -8 yalign 1.0 yoffset -8 action Show('artist_details', gal_item=gal_item):
                                idle 'info_button_idle'
                                hover 'gui/info button.png'
            for j in range(i, (cg_page+1)*gal_cells): #we need this to fully fill the grid
                null
    vbox:
        style_group "navi"
        xalign 0.37
        yalign 0.925

        hbox at nav_eff:
            xsize 525
            spacing 10
            if cg_page > 0:
                textbutton _("Previous") action [If(cg_page > 0, true=SetScreenVariable('cg_page', cg_page - 1), false=NullAction()), With(dissolve)] xalign 0.0
            if len(cg_seq) > gal_cells:
                textbutton _("Next") action (SetScreenVariable('cg_page', next_cg_page), With(dissolve)) xalign 1.0
    use progress


screen progress():
    # TODO: this screen seems never be displayed due to this check, fix when game progress indicator will be needed
    if not renpy.context()._main_menu:
        $ current_progress = PercentComplete()
        hbox:
            style_group "bonus"
            xalign .2 yalign 0.8
            #bar value current_progress range 100 xmaximum 150 thumb None thumb_shadow None
            text (str(current_progress)+'%')


# show detais for choosen image
screen artist_details(gal_item):
    modal True
    frame:
        # shadow screens below
        xfill True
        yfill True
        background '#0008'
        frame:
            style_group "navi"
            background Frame("gui/frame2.png",24,24)
            xalign 0.5
            yalign 0.5
            xpadding 25
            ypadding 25
            vbox:
                text 'Image name'
                text artists_info[gal_item][0] size 30
                text 'Artist'
                text artists_info[gal_item][1] size 30
                # if artist has website, show it
                if artists_info[gal_item][2]:
                    text 'Website'
                    $ ui.text('{{a={}}}{}{{/a}}'.format(artists_info[gal_item][2], artists_info[gal_item][2]), size=30)
                # button for closing this screen
                textbutton _('Return') action Hide('artist_details') at nav_eff


########################################################################################################################
#### MUSIC ROOM #######################################################################################################
########################################################################################################################
init python:
    mr = MusicRoom(fadeout=1.0)
    mr.add("music/title screen loop.ogg")
    mr.add("music/village loop.ogg")
    mr.add("music/Jezera 1 loop.ogg")
    mr.add("music/Orc Ambush loop.ogg")
    mr.add("music/Jezera 2 loop.ogg")
    mr.add("music/burning village loop.ogg")
    mr.add("music/destroyed village loop.ogg")
    mr.add("music/before the gates loop.ogg")
    mr.add("music/track9.mp3")
    mr.add("music/track10.mp3")
    mr.add("music/track11.mp3")
    mr.add("music/track12.mp3")


    track_playing = "Track 1"
    track_length = "3.14"


screen music_room:
    tag menu
    add "gui/gm_back.jpg"
    use bonus_navigation
    vbox:
        add "gui/frame.png"
        xalign 0.05
        yalign 0.5
    vbox:
        xalign 0.18
        yalign 0.5
        add "gui/jukebox.png"
    vbox:
        xalign 0.22
        yalign 0.675
        hbox:
            xalign 0.5
            vbox:
                style_group "navi"
                textbutton "Seeds of Chaos" action [SetVariable("track_length", "1.19"), SetVariable("track_playing", "Track 1"), mr.Play("music/title screen loop.ogg")] at nav_eff
                textbutton "Village Breeze" action [SetVariable("track_length", "1.41"), SetVariable("track_playing", "Track 2"), mr.Play("music/village loop.ogg")] at nav_eff
                textbutton "Woman in Red" action [SetVariable("track_length", "2.00"), SetVariable("track_playing", "Track 3"), mr.Play("music/Jezera 1 loop.ogg")] at nav_eff
                textbutton "Forest Ambush" action [SetVariable("track_length", "1.23"), SetVariable("track_playing", "Track 4"), mr.Play("music/Orc Ambush loop.ogg")] at nav_eff
            null width 20
            vbox:
                style_group "navi"
                textbutton "The Truth Revealed" action [SetVariable("track_length", "1.51"), SetVariable("track_playing", "Track 5"), mr.Play("music/Jezera 2 loop.ogg")] at nav_eff
                textbutton "Smoke and Flame" action [SetVariable("track_length", "1.59"), SetVariable("track_playing", "Track 6"), mr.Play("music/burning village loop.ogg")] at nav_eff
                textbutton "The Wind Replies" action [SetVariable("track_length", "1.59"), SetVariable("track_playing", "Track 7"), mr.Play("music/destroyed village loop.ogg")] at nav_eff
                textbutton "Before the Gates" action [SetVariable("track_length", "1.43"), SetVariable("track_playing", "Track 8"), mr.Play("music/before the gates loop.ogg")] at nav_eff
            null width 20
            vbox:
                style_group "navi"
                textbutton "???" action [SetVariable("track_length", "3.14"), SetVariable("track_playing", "Track 9"), mr.Play("music/track9.mp3")] at nav_eff
                textbutton "???" action [SetVariable("track_length", "3.14"), SetVariable("track_playing", "Track 10"), mr.Play("music/track10.mp3")] at nav_eff
                textbutton "???" action [SetVariable("track_length", "3.14"), SetVariable("track_playing", "Track 11"), mr.Play("music/track11.mp3")] at nav_eff
                textbutton "???" action [SetVariable("track_length", "3.14"), SetVariable("track_playing", "Track 12"), mr.Play("music/track12.mp3")] at nav_eff

    vbox:
        xalign 0.42
        yalign 0.243
        text "{size=40}{b}Currently Playing:{/b}{/size}"
    vbox:
        xalign 0.37
        yalign 0.358
        text "{k=8}{size=25}[track_playing]{/size}{/k}"
    vbox:
        xalign 0.655
        yalign 0.358
        text "{k=8}{size=25}[track_length]{/size}{/k}"

    on "replace" action mr.Play()
    on "replaced" action Play("music", "music/track1.mp3")

########################################################################################################################
#### SCENE REPLAY #######################################################################################################
########################################################################################################################


init:
    image scene_replay1 = im.Scale("images/CG/RowanxAlexia 1.png", thumbnail_x, thumbnail_y)
    image scene_replay2 = im.Scale("images/CG/JezeraxRowan 1.png", thumbnail_x, thumbnail_y)
    image scene_replay3 = im.Scale("images/CG/AndrasxRowan 1.png", thumbnail_x, thumbnail_y)
    image scene_replay4 = im.Scale("images/CG/AlxAn Anal 1.png", thumbnail_x, thumbnail_y)
    image scene_replay5 = im.Scale("images/CG/RowanxAlexia 2 4.png", thumbnail_x, thumbnail_y)
    image scene_lock = im.Scale("gui/gallocked.png", thumbnail_x, thumbnail_y)

    # scenes to replay. format - tuple of tuples: ((persistent_var, scene_label, thumbnail, <dict of vars used in that scene>), ...)
    $ replay_scenes = (('sex_scene1', 'sexscene1', 'scene_replay1', {}),
                        ('sex_scene2', 'sexscene2', 'scene_replay2', {'jezera_name': 'Jezera'}),
                        ('sex_scene3', 'sexscene3', 'scene_replay3', {}),
                        ('sex_scene4', 'sexscene4', 'scene_replay4', {}),
                        ('sex_scene5', 'sexscene5', 'scene_replay5', {}),
                        ('dummy', 'dummy', 'dummy', {}),
                        ('dummy', 'dummy', 'dummy', {}), ('dummy', 'dummy', 'dummy', {}), ('dummy', 'dummy', 'dummy', {}),
                        ('dummy', 'dummy', 'dummy', {}), ('dummy', 'dummy', 'dummy', {}),)


screen scene_replay():
    default gal_rows = 3
    default gal_cols = 3
    default gal_cells = gal_rows * gal_cols
    default rp_page = 0
    tag menu
    add "gui/gm_back.jpg"
    use bonus_navigation
    vbox:
        add "gui/frame.png"
        xalign 0.05
        yalign 0.5
    # grid of replay scene buttons - dimensions same as in cg_gallery
    grid gal_rows gal_cols:
        xpos 70
        ypos 90
        $ i = 0
        # loop through all replay scenes
        for rp_item in replay_scenes:
            $ i += 1
            # if scene belongs to current page, display a button for it
            if i <= (rp_page+1)*gal_cells and i>rp_page*gal_cells:
                fixed:
                    xysize (thumbnail_x+22, thumbnail_y+22)
                    # check if persistent variable for this scene is triggered in game
                    if getattr(persistent, rp_item[0], None):
                        # if scene unlocked, display Replay button
                        imagebutton action Replay(rp_item[1], scope=rp_item[3]) background Frame("gui/frame2.png",24,24) align (0.5, 0.5) xpadding 8 ypadding 8 at scene_replay_eff:
                            idle im.Composite((thumbnail_x, thumbnail_y), (0,0), ImageReference(rp_item[2]), (0,0), "gui/gallery_border.png")
                    else:
                        # if scene still locked, display NullAction button with 'locked' image
                        imagebutton idle "scene_lock" action NullAction() background Frame("gui/frame2.png",24,24) align (0.5, 0.5) xpadding 8 ypadding 8 at scene_replay_eff
        # if there are not enough scenes for current page, populate grid with null displaybles
        for j in range(i, (rp_page+1)*gal_cells): #we need this to fully fill the grid
            null
    vbox:
        style_group "navi"
        xalign 0.37
        yalign 0.925
        $ next_rp_page = rp_page + 1
        # if this is a last page, set 'next page' button to jump to first page
        if next_rp_page > int(len(replay_scenes)/gal_cells):
            $ next_rp_page = 0
        # if there are replay scenes only for one page, do not display 'Next Page' button

        hbox at nav_eff:
            xsize 525
            spacing 10
            if rp_page > 0:
                textbutton _("Previous") action [If(rp_page > 0, true=SetScreenVariable('rp_page', rp_page - 1), false=NullAction()), With(dissolve)] xalign 0.0
            if len(replay_scenes) > gal_cells:
                textbutton _("Next") action (SetScreenVariable('rp_page', next_rp_page), With(dissolve)) xalign 1.0
