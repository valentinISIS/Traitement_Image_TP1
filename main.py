import skimage.io as io
import skimage.color as color
import skimage.exposure as exposure
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    print("-----------------------------Introduction-----------------------------")

    """ Sauvegarde 'd'une image"""
    chem_lena = '/lena.tiff'
    img_lena = io.imread('images-TP1'+chem_lena)
    io.imsave('Log'+chem_lena, img_lena)
    print("Image lena sauvegardée")

    """ Sauvegarde 'd'une image en gris"""
    chem_lena_gray = '/lena_gray.tiff'
    img_lena_gray = color.rgb2gray(img_lena)
    io.imsave("Log"+chem_lena_gray, img_lena_gray)
    print("Image lena en gris sauvegardée")

    """ Sauvegarde 'd'une image en hsv"""
    chem_lena_hsv = '/lena_hsv.tiff'
    img_lena_hsv = color.rgb2hsv(img_lena)
    io.imsave("Log" + chem_lena_hsv, img_lena_hsv)
    print("Image lena en hsv sauvegardée")

    """ Sauvegarde 'd'une image en lab"""
    chem_lena_lab = '/lena_lab.tiff'
    img_lena_lab = color.rgb2lab(img_lena)
    io.imsave("Log" + chem_lena_lab, img_lena_lab)
    print("Image lena en lab sauvegardée")

    """Histograme du rouge de la ligne 200"""
    nLigne = 200
    chem_plan_rouge_nLigne = '/profile_rouge_ligne'+str(nLigne)
    """
    Cette ligne permet de réccupérer la ligne 'nLigne' dans la première matrice (rouge)
    Les ':' permet de spécifier qu'on prends toute la ligne
    Si on veut prendre prendre une colone il faut écrire par exemple img_lena[:, 200, 0]
    """
    plan_rouge_nLigne = img_lena[nLigne, :, 0]

    """Ces lignes permettent de sauvegarder l'histograme grace à la librairie mathplotlib"""
    fig, ax = plt.subplots()
    ax.plot(plan_rouge_nLigne, color='k')
    plt.savefig('Log'+chem_plan_rouge_nLigne)
    print("Profil couleur rouge ligne " + str(nLigne) + " sauvegardé")

    print("\n-----------------------------Exercice 1-----------------------------")
    """Création d'une image en niveau de gris"""
    chem_forest = '/forest.png'
    chem_forest_gray = '/forest_gray.tiff'
    img_forest = io.imread('images-TP1' + chem_forest)
    img_forest_gray = color.rgb2gray(img_forest)
    io.imsave('Log' + chem_forest_gray, img_forest_gray)
    print("Image forest en gris sauvegardée")

    """Création d'un histograme de niveau de gris"""
    nbins = 256
    chem_histogram_forest_gray = '/histogram_forest_gray.tiff'
    """
    Cette ligne permet d'établir l'histograme des niveau de gris d'une matrice (une image en niveau de couleur)
    La fonction 'exposure.histogram' renvoie un tuple, il est donc important de stocker les 2 données dans deux 
    variables
    spécifier nbins permet de régler le nombre de barre
    """
    histogram_forest_gray, histogram_forest_gray_centers = exposure.histogram(img_forest_gray, nbins=nbins)
    """
    Ces lignes permettent d'enregistrer l'histograme
    Il est important d'utiser ax.bar à la place de ax.plot pour l'affichage
    ax.bar demande comme premier paramètre une liste de valeur, on ajoute donc une liste allant de 0 à nbins pour 
    représenter les valeurs
    """
    fig2, ax = plt.subplots()
    ax.bar([i for i in range(nbins)], histogram_forest_gray, color='k')
    plt.savefig('Log'+chem_histogram_forest_gray)
    print("Histograme de niveau de gris sauvegardé")

    """
    Création d'une image contrastée
    -> Plus le coefficient est grand, plus l'image sera blanche
    -> Plus le coefficient est bas, plus l'image sera noir
    """
    coefficient = 1.2
    chem_forest_contraste = '/forest_contraste.tiff'
    img_forest_contraste = color.rgb2gray(img_forest)
    """
    Parcours de toutes les valeurs de la matrice de l'image
    Pour réccupérer les valeurs, on réccupère les positions en utilisant
                                                            -> 'img.shape[0] pour les colones'
                                                            -> 'img.shape[1] pour les lignes'
    """
    for i in range(img_forest_contraste.shape[0]):
        for j in range(img_forest_contraste.shape[1]):
            """
            On vient multiplier la valeur à la position par le coefficient
            Si la valeur dépasse 1, la valeur revient à 1
            """
            img_forest_contraste[i, j] = min(1, img_forest_contraste[i, j]*coefficient)
    io.imsave('Log' + chem_forest_contraste, img_forest_contraste)
    print("Image forest contrastée sauvegardée")

    """
    Création d'une image en noir et blanc par rapport à un seuil
    -> Plus le seuil est grand, plus l'image sera noir
    -> Moins le seuil est grand, plus l'image sera blanche
    """
    seuil = 0.6
    chem_forest_noir_blanc = '/forest_noir_blanc.tiff'
    img_forest_noir_blanc = color.rgb2gray(img_forest)
    """
        Parcours de toutes les valeurs de la matrice de l'image
        Pour réccupérer les valeurs, on réccupère les positions en utilisant
                                                                -> 'img.shape[0] pour les colones'
                                                                -> 'img.shape[1] pour les lignes'
        """
    for i in range(img_forest_noir_blanc.shape[0]):
        for j in range(img_forest_noir_blanc.shape[1]):
            """
            Cette ligne remplie la fonction:
            -> La valeur devient 1 si la valeur est supérieur au seuil
            -> La valeur devient 0 sinon
            On utilise la stratégie que True = 1 et False = 0 quand on les caste en entier
            """
            img_forest_noir_blanc[i, j] = int(img_forest_contraste[i, j] > seuil)
    io.imsave('Log' + chem_forest_noir_blanc, img_forest_noir_blanc)
    print("Image noir et blanc contrastée sauvegardée")
