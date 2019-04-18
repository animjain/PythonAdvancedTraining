class PageView:
    def __init__(self, role="user"):
        self.role = role

    def __getattr__(self, attr):
        if self.role == 'admin':
            def getstats():
                print "This is admin statistics..."

            def adduser():
                print "Add user functionality for admin..."

            if attr == 'getstats':
                return getstats
            elif attr == 'adduser':
                return adduser

        elif self.role == 'user':
            def getstats():
                print "This is user statistics..."

            def show_home():
                print "Showing user home page..."

            if attr == 'getstats':
                return getstats
            elif attr == 'show_home':
                return show_home


if __name__ == '__main__':
    p = PageView()
    print(p)

