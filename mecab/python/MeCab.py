# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.40
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.
# This file is compatible with both classic and new-style classes.

from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_MeCab', [dirname(__file__)])
        except ImportError:
            import _MeCab
            return _MeCab
        if fp is not None:
            try:
                _mod = imp.load_module('_MeCab', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _MeCab = swig_import_helper()
    del swig_import_helper
else:
    import _MeCab
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class DictionaryInfo(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, DictionaryInfo, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DictionaryInfo, name)
    __repr__ = _swig_repr
    __swig_getmethods__["filename"] = _MeCab.DictionaryInfo_filename_get
    if _newclass:filename = _swig_property(_MeCab.DictionaryInfo_filename_get)
    __swig_getmethods__["charset"] = _MeCab.DictionaryInfo_charset_get
    if _newclass:charset = _swig_property(_MeCab.DictionaryInfo_charset_get)
    __swig_getmethods__["size"] = _MeCab.DictionaryInfo_size_get
    if _newclass:size = _swig_property(_MeCab.DictionaryInfo_size_get)
    __swig_getmethods__["type"] = _MeCab.DictionaryInfo_type_get
    if _newclass:type = _swig_property(_MeCab.DictionaryInfo_type_get)
    __swig_getmethods__["lsize"] = _MeCab.DictionaryInfo_lsize_get
    if _newclass:lsize = _swig_property(_MeCab.DictionaryInfo_lsize_get)
    __swig_getmethods__["rsize"] = _MeCab.DictionaryInfo_rsize_get
    if _newclass:rsize = _swig_property(_MeCab.DictionaryInfo_rsize_get)
    __swig_getmethods__["version"] = _MeCab.DictionaryInfo_version_get
    if _newclass:version = _swig_property(_MeCab.DictionaryInfo_version_get)
    __swig_getmethods__["next"] = _MeCab.DictionaryInfo_next_get
    if _newclass:next = _swig_property(_MeCab.DictionaryInfo_next_get)
    def __init__(self): 
        this = _MeCab.new_DictionaryInfo()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _MeCab.delete_DictionaryInfo
    __del__ = lambda self : None;
DictionaryInfo_swigregister = _MeCab.DictionaryInfo_swigregister
DictionaryInfo_swigregister(DictionaryInfo)

class Path(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Path, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Path, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_getmethods__["rnode"] = _MeCab.Path_rnode_get
    if _newclass:rnode = _swig_property(_MeCab.Path_rnode_get)
    __swig_getmethods__["rnext"] = _MeCab.Path_rnext_get
    if _newclass:rnext = _swig_property(_MeCab.Path_rnext_get)
    __swig_getmethods__["lnode"] = _MeCab.Path_lnode_get
    if _newclass:lnode = _swig_property(_MeCab.Path_lnode_get)
    __swig_getmethods__["lnext"] = _MeCab.Path_lnext_get
    if _newclass:lnext = _swig_property(_MeCab.Path_lnext_get)
    __swig_getmethods__["cost"] = _MeCab.Path_cost_get
    if _newclass:cost = _swig_property(_MeCab.Path_cost_get)
    __swig_setmethods__["prob"] = _MeCab.Path_prob_set
    __swig_getmethods__["prob"] = _MeCab.Path_prob_get
    if _newclass:prob = _swig_property(_MeCab.Path_prob_get, _MeCab.Path_prob_set)
Path_swigregister = _MeCab.Path_swigregister
Path_swigregister(Path)

class Token(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Token, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Token, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_getmethods__["lcAttr"] = _MeCab.Token_lcAttr_get
    if _newclass:lcAttr = _swig_property(_MeCab.Token_lcAttr_get)
    __swig_getmethods__["rcAttr"] = _MeCab.Token_rcAttr_get
    if _newclass:rcAttr = _swig_property(_MeCab.Token_rcAttr_get)
    __swig_getmethods__["posid"] = _MeCab.Token_posid_get
    if _newclass:posid = _swig_property(_MeCab.Token_posid_get)
    __swig_getmethods__["wcost"] = _MeCab.Token_wcost_get
    if _newclass:wcost = _swig_property(_MeCab.Token_wcost_get)
    __swig_getmethods__["feature"] = _MeCab.Token_feature_get
    if _newclass:feature = _swig_property(_MeCab.Token_feature_get)
    __swig_getmethods__["compound"] = _MeCab.Token_compound_get
    if _newclass:compound = _swig_property(_MeCab.Token_compound_get)
Token_swigregister = _MeCab.Token_swigregister
Token_swigregister(Token)

class Node(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Node, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Node, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_getmethods__["prev"] = _MeCab.Node_prev_get
    if _newclass:prev = _swig_property(_MeCab.Node_prev_get)
    __swig_getmethods__["next"] = _MeCab.Node_next_get
    if _newclass:next = _swig_property(_MeCab.Node_next_get)
    __swig_getmethods__["enext"] = _MeCab.Node_enext_get
    if _newclass:enext = _swig_property(_MeCab.Node_enext_get)
    __swig_getmethods__["bnext"] = _MeCab.Node_bnext_get
    if _newclass:bnext = _swig_property(_MeCab.Node_bnext_get)
    __swig_getmethods__["rpath"] = _MeCab.Node_rpath_get
    if _newclass:rpath = _swig_property(_MeCab.Node_rpath_get)
    __swig_getmethods__["lpath"] = _MeCab.Node_lpath_get
    if _newclass:lpath = _swig_property(_MeCab.Node_lpath_get)
    __swig_getmethods__["feature"] = _MeCab.Node_feature_get
    if _newclass:feature = _swig_property(_MeCab.Node_feature_get)
    __swig_getmethods__["id"] = _MeCab.Node_id_get
    if _newclass:id = _swig_property(_MeCab.Node_id_get)
    __swig_getmethods__["length"] = _MeCab.Node_length_get
    if _newclass:length = _swig_property(_MeCab.Node_length_get)
    __swig_getmethods__["rlength"] = _MeCab.Node_rlength_get
    if _newclass:rlength = _swig_property(_MeCab.Node_rlength_get)
    __swig_getmethods__["rcAttr"] = _MeCab.Node_rcAttr_get
    if _newclass:rcAttr = _swig_property(_MeCab.Node_rcAttr_get)
    __swig_getmethods__["lcAttr"] = _MeCab.Node_lcAttr_get
    if _newclass:lcAttr = _swig_property(_MeCab.Node_lcAttr_get)
    __swig_getmethods__["posid"] = _MeCab.Node_posid_get
    if _newclass:posid = _swig_property(_MeCab.Node_posid_get)
    __swig_getmethods__["char_type"] = _MeCab.Node_char_type_get
    if _newclass:char_type = _swig_property(_MeCab.Node_char_type_get)
    __swig_getmethods__["stat"] = _MeCab.Node_stat_get
    if _newclass:stat = _swig_property(_MeCab.Node_stat_get)
    __swig_getmethods__["isbest"] = _MeCab.Node_isbest_get
    if _newclass:isbest = _swig_property(_MeCab.Node_isbest_get)
    __swig_getmethods__["alpha"] = _MeCab.Node_alpha_get
    if _newclass:alpha = _swig_property(_MeCab.Node_alpha_get)
    __swig_getmethods__["beta"] = _MeCab.Node_beta_get
    if _newclass:beta = _swig_property(_MeCab.Node_beta_get)
    __swig_setmethods__["prob"] = _MeCab.Node_prob_set
    __swig_getmethods__["prob"] = _MeCab.Node_prob_get
    if _newclass:prob = _swig_property(_MeCab.Node_prob_get, _MeCab.Node_prob_set)
    __swig_getmethods__["wcost"] = _MeCab.Node_wcost_get
    if _newclass:wcost = _swig_property(_MeCab.Node_wcost_get)
    __swig_getmethods__["cost"] = _MeCab.Node_cost_get
    if _newclass:cost = _swig_property(_MeCab.Node_cost_get)
    __swig_getmethods__["token"] = _MeCab.Node_token_get
    if _newclass:token = _swig_property(_MeCab.Node_token_get)
    __swig_getmethods__["surface"] = _MeCab.Node_surface_get
    if _newclass:surface = _swig_property(_MeCab.Node_surface_get)
Node_swigregister = _MeCab.Node_swigregister
Node_swigregister(Node)

MECAB_NOR_NODE = _MeCab.MECAB_NOR_NODE
MECAB_UNK_NODE = _MeCab.MECAB_UNK_NODE
MECAB_BOS_NODE = _MeCab.MECAB_BOS_NODE
MECAB_EOS_NODE = _MeCab.MECAB_EOS_NODE
MECAB_EON_NODE = _MeCab.MECAB_EON_NODE
MECAB_USR_DIC = _MeCab.MECAB_USR_DIC
MECAB_SYS_DIC = _MeCab.MECAB_SYS_DIC
MECAB_UNK_DIC = _MeCab.MECAB_UNK_DIC
MECAB_ONE_BEST = _MeCab.MECAB_ONE_BEST
MECAB_NBEST = _MeCab.MECAB_NBEST
MECAB_PARTIAL = _MeCab.MECAB_PARTIAL
MECAB_MARGINAL_PROB = _MeCab.MECAB_MARGINAL_PROB
MECAB_ALTERNATIVE = _MeCab.MECAB_ALTERNATIVE
MECAB_ALL_MORPHS = _MeCab.MECAB_ALL_MORPHS
MECAB_ALLOCATE_SENTENCE = _MeCab.MECAB_ALLOCATE_SENTENCE
class Lattice(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Lattice, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Lattice, name)
    __repr__ = _swig_repr
    def clear(self): return _MeCab.Lattice_clear(self)
    def is_available(self): return _MeCab.Lattice_is_available(self)
    def bos_node(self): return _MeCab.Lattice_bos_node(self)
    def eos_node(self): return _MeCab.Lattice_eos_node(self)
    def end_nodes(self, *args): return _MeCab.Lattice_end_nodes(self, *args)
    def begin_nodes(self, *args): return _MeCab.Lattice_begin_nodes(self, *args)
    def sentence(self): return _MeCab.Lattice_sentence(self)
    def size(self): return _MeCab.Lattice_size(self)
    def set_Z(self, *args): return _MeCab.Lattice_set_Z(self, *args)
    def Z(self): return _MeCab.Lattice_Z(self)
    def set_theta(self, *args): return _MeCab.Lattice_set_theta(self, *args)
    def theta(self): return _MeCab.Lattice_theta(self)
    def next(self): return _MeCab.Lattice_next(self)
    def request_type(self): return _MeCab.Lattice_request_type(self)
    def has_request_type(self, *args): return _MeCab.Lattice_has_request_type(self, *args)
    def set_request_type(self, *args): return _MeCab.Lattice_set_request_type(self, *args)
    def add_request_type(self, *args): return _MeCab.Lattice_add_request_type(self, *args)
    def remove_request_type(self, *args): return _MeCab.Lattice_remove_request_type(self, *args)
    def toString(self, *args): return _MeCab.Lattice_toString(self, *args)
    def enumNBestAsString(self, *args): return _MeCab.Lattice_enumNBestAsString(self, *args)
    def what(self): return _MeCab.Lattice_what(self)
    def set_what(self, *args): return _MeCab.Lattice_set_what(self, *args)
    __swig_destroy__ = _MeCab.delete_Lattice
    __del__ = lambda self : None;
    def __init__(self): 
        this = _MeCab.new_Lattice()
        try: self.this.append(this)
        except: self.this = this
    def set_sentence(self, *args): return _MeCab.Lattice_set_sentence(self, *args)
Lattice_swigregister = _MeCab.Lattice_swigregister
Lattice_swigregister(Lattice)

class Model(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Model, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Model, name)
    __repr__ = _swig_repr
    def dictionary_info(self): return _MeCab.Model_dictionary_info(self)
    def createTagger(self): return _MeCab.Model_createTagger(self)
    def createLattice(self): return _MeCab.Model_createLattice(self)
    __swig_getmethods__["version"] = lambda x: _MeCab.Model_version
    if _newclass:version = staticmethod(_MeCab.Model_version)
    __swig_destroy__ = _MeCab.delete_Model
    __del__ = lambda self : None;
    __swig_getmethods__["create"] = lambda x: _MeCab.Model_create
    if _newclass:create = staticmethod(_MeCab.Model_create)
    def __init__(self, *args): 
        this = _MeCab.new_Model(*args)
        try: self.this.append(this)
        except: self.this = this
Model_swigregister = _MeCab.Model_swigregister
Model_swigregister(Model)

def Model_version():
  return _MeCab.Model_version()
Model_version = _MeCab.Model_version

def Model_create(*args):
  return _MeCab.Model_create(*args)
Model_create = _MeCab.Model_create

class Tagger(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Tagger, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Tagger, name)
    __repr__ = _swig_repr
    def parse(self, *args): return _MeCab.Tagger_parse(self, *args)
    def parseToNode(self, *args): return _MeCab.Tagger_parseToNode(self, *args)
    def parseNBest(self, *args): return _MeCab.Tagger_parseNBest(self, *args)
    def parseNBestInit(self, *args): return _MeCab.Tagger_parseNBestInit(self, *args)
    def nextNode(self): return _MeCab.Tagger_nextNode(self)
    def next(self): return _MeCab.Tagger_next(self)
    def formatNode(self, *args): return _MeCab.Tagger_formatNode(self, *args)
    def set_request_type(self, *args): return _MeCab.Tagger_set_request_type(self, *args)
    def request_type(self): return _MeCab.Tagger_request_type(self)
    def partial(self): return _MeCab.Tagger_partial(self)
    def set_partial(self, *args): return _MeCab.Tagger_set_partial(self, *args)
    def lattice_level(self): return _MeCab.Tagger_lattice_level(self)
    def set_lattice_level(self, *args): return _MeCab.Tagger_set_lattice_level(self, *args)
    def all_morphs(self): return _MeCab.Tagger_all_morphs(self)
    def set_all_morphs(self, *args): return _MeCab.Tagger_set_all_morphs(self, *args)
    def set_theta(self, *args): return _MeCab.Tagger_set_theta(self, *args)
    def theta(self): return _MeCab.Tagger_theta(self)
    def dictionary_info(self): return _MeCab.Tagger_dictionary_info(self)
    def what(self): return _MeCab.Tagger_what(self)
    __swig_destroy__ = _MeCab.delete_Tagger
    __del__ = lambda self : None;
    __swig_getmethods__["create"] = lambda x: _MeCab.Tagger_create
    if _newclass:create = staticmethod(_MeCab.Tagger_create)
    __swig_getmethods__["version"] = lambda x: _MeCab.Tagger_version
    if _newclass:version = staticmethod(_MeCab.Tagger_version)
    def __init__(self, *args): 
        this = _MeCab.new_Tagger(*args)
        try: self.this.append(this)
        except: self.this = this
    def parseToString(self, *args): return _MeCab.Tagger_parseToString(self, *args)
Tagger_swigregister = _MeCab.Tagger_swigregister
Tagger_swigregister(Tagger)

def Tagger_create(*args):
  return _MeCab.Tagger_create(*args)
Tagger_create = _MeCab.Tagger_create

def Tagger_version():
  return _MeCab.Tagger_version()
Tagger_version = _MeCab.Tagger_version

VERSION = _MeCab.VERSION


