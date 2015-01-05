#encoding:shift-jis
from __future__ import division, print_function
__metaclass__ = type
import nose
from nose.tools import *
from sffairmaker.item_scroll_bar import *

def test():
    app = QApplication([])
    scr = ItemScrollBar()
    
    log = []
    scr.currentItemChanged.connect(log.append)
    assert_equal(scr.currentItem(), None)
    assert_equal(scr.items(), [])
    
    #�󃊃X�g��ݒ肷��ƁA�l�̓f�t�H���g�l
    scr.setItems([])
    assert_equal(scr.currentItem(), None)
    assert_equal(scr.items(), [])
    assert_equal(log, [])
    log[:] = []
    
    #��łȂ����X�g��ݒ肷��ƁA�l�͍ŏ��̗v�f
    scr.setItems([1, 2, 3, 4, 5])
    assert_equal(scr.currentItem(), 1)
    assert_equal(scr.items(), [1, 2, 3, 4, 5])
    assert_equal(log, [1])
    log[:] = []
    
    #�������X�g��ݒ肵�Ă������N����Ȃ�
    scr.setItems([1, 2, 3, 4, 5])
    assert_equal(scr.currentItem(), 1)
    assert_equal(scr.items(), [1, 2, 3, 4, 5])
    assert_equal(log, [])
    log[:] = []
    
    #�O�w���Ă����v�f���V�������X�g�ɖ����ƁA�O�̃��X�g�ň���ɂ������v�f���w��
    scr.setItems([1, 2, 3, 4, 5])
    scr.setCurrentItem(3)
    log[:] = []
    
    scr.setItems([1, 2, "spam", 4, 5])
    assert_equal(scr.currentItem(), 2, scr.currentItem())
    assert_equal(scr.items(), [1, 2, "spam", 4, 5])
    assert_equal(log, [2], log)
    log[:] = []
    
    #�O�w���Ă����v�f���V�������X�g�ɖ����A�O�̃��X�g�ň�ԍ����w���Ă����Ƃ��A
    #�E�ɂ������v�f���w��
    scr.setItems([3, 4, 5, 6])
    scr.setCurrentItem(3)
    log[:] = []
    
    scr.setItems(["spam", 4, 5, 6])
    assert_equal(scr.currentItem(), 4)
    assert_equal(scr.items(), ["spam", 4, 5, 6])
    assert_equal(log, [4])
    log[:] = []
    
    #�V�������X�g���A�O�̃��X�g�Ƌ��ʂ̗v�f��S�������Ȃ��Ƃ��A
    #��ԍŏ��̗v�f�������B
    scr.setItems(list("abcdefg"))
    assert_equal(scr.currentItem(), "a")
    assert_equal(scr.items(), list("abcdefg"))
    assert_equal(log, ["a"], log)
    log[:] = []
    
    #�d������v�f�͔r��
    scr.setItems(list("abcaaa"))
    assert_equal(scr.items(), list("abc"))
    
    
def main():
    nose.runmodule()
if __name__ == '__main__':
    main()
