
from createdb import Jiji, Limarket, Soumary
#test


def Recu_info(name):
    limarke=Limarket.query.filter(Limarket.li_name.contains(name)).all()
    jiji=Jiji.query.filter(Jiji.ji_name.contains(name)).all()
    soumari=Soumary.query.filter(Soumary.soumary_name.contains(name)).all()
    return limarke , jiji, soumari
