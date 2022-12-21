{
    'name': "Homestay", # tên module
    'name_vi_VN': "Homestay_vi_VN",# tên bằng tiếng việt
    'summary': """ Summary  """,# mô tả ngắn gọn module 
    'description': """Description""", # mô tả chi tiết module, tính năng bằng tiếng anh
    'description_vi_VN': """Description_Vn""",# mô tả chi tiết module, tính năng bằng tiếng việt
    'author': "Viindoo", # tác giả module
    'website': "https://viindoo.com", #website chứa thêm thông tin của module
    'live_test_url': "https://v14demo-int.viindoo.com",
    'live_test_url_vi_VN': "https://v14demo-vn.viindoo.com",
    'support': "apps.support@viindoo.com",
    'category': 'Uncategorized', # loại module
    'version': '0.1.0', # phiên bản app
    'depends': ['base'], # nơi khai báo app/module khác mà mình sẽ phụ thuộc 
    'data': [
        # 'security/security.xml',
        # 'security/ir.model.access.csv',
        # 'views/kethua.xml',
        'views/invoice.xml',
        'views/room.xml',
        'views/service.xml',
        'views/roomService.xml',
        'views/guest.xml',
        'views/booking.xml',
        'wizard/invoice_winzard_views.xml',
        # 'views/chanea.xml',
        
        # 'data/author.xml',
        # 'data/home.xml',
        # 'data/room.xml'
        
    ], # Khai báo view và config phân quyền
    'demo': [
        # 'demo/demo.xml',
    ],
     'qweb': [
        #'static/src/xml/*.xml',
        # 'static/description/testButton.xml', # <-- khai bao thua ke qweb vua hien thuc
    ],
    'images' : [
        ],
    'installable': True, #Cài đặt được
    'sequence': -1000,
    'application': True, # Chuyển vào filter App
    'auto_install': False,  #  
    'price': 99.9,
    'currency': 'EUR',
    'license': 'OPL-1',
}
