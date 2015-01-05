#encoding:shift-jis
from __future__ import division, print_function
__metaclass__ = type
import nose, nose.tools
from sffairmaker.clsn_text_edit import *

def test():
    app = QApplication([])
    from pprint import pformat
    r = ClsnTextEdit()
    def rect(left, top, right, bottom):
        return QRect(QPoint(left, top), QPoint(right, bottom))
    
    r.setText("")
    assert r.value() == Clsn()
    
    log = []
    r.valueChanged.connect(log.append)
    t = "2, 3, 5, 7\n11, 13, 17, 19"
    r.setText(t)
    v = Clsn([rect(2, 3, 5, 7), rect(11, 13, 17, 19)])
    
    assert r.value() == v, pformat(r.value()) + "\n" + pformat(v)
    assert log == [v], pformat(log) + "\n" + pformat([v])
    assert r.text() == t
    
    log[:] = []
    # texts���ς���Ă��\������rects�������Ȃ�A�V�O�i���͔��s����Ȃ�
    t = "2, +3, 5, 7  ;spam\n\n11, 13,17,19"
    r.setText(t)
    assert log == []
    assert r.text() == t
    assert r.value() == Clsn([rect(2, 3, 5, 7), rect(11, 13, 17, 19)])
    
    log[:] = []
    # rects���ς��Ȃ���΁Atext�͍X�V����Ȃ��B
    r.setValue(Clsn([rect(2, 3, 5, 7), rect(11, 13, 17, 19)]))
    assert log == []
    assert r.text() == t
    assert r.value() == Clsn([rect(2, 3, 5, 7), rect(11, 13, 17, 19)])


def main():
    nose.runmodule()
if __name__ == '__main__':
    main()
