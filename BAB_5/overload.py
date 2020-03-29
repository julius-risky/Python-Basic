#mendefinisikan fungsi bagi()
def bagi(bil1,bil2):
    if isinstance(bil1,int) and isinstance(bil2,int):
        return bil1 // bil2
    else:
        return bil1/bil2

