function wrapping(gifts) {
    const giftWrapping = gifts.map(i => i.length+2)
    const gift
    .repeat()
    return giftWrapping
}


const gifts = ['cat', 'game', 'socks']

const cloneGifts = [...gifts] 

const wrapped = wrapping(cloneGifts)
console.log(wrapped)



// [
//   "*****\n*cat*\n*****",
//   "******\n*game*\n******",
//   "*******\n*socks*\n*******"
// ] 