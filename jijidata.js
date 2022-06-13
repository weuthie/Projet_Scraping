const ppt = require("puppeteer")
const {Pool,Client} = require("pg")
const pool = new Pool(
    {
        host:"localhost",
        user:"groupe4",
        port:5432,
        password:"test123",
        database:"scraping"
    }
)
async function recupDonne() {
    const navigateur = await ppt.launch({headless:false})
    const page = await navigateur.newPage()
    await page.goto("https://www.alloallo.com/sn/search/?q=iphone")
    let allo = await page.evaluate(async ()=>{  
        const produits = document.querySelectorAll(".col-xl-3.col-lg-3.col-md-4.col-sm-6.col-6")
        let allo = []
        produits.forEach(produit => {
            let ite_data={}
            ite_data.image = produit.querySelector("img").getAttribute("src")
            ite_data.namee = produit.querySelector(".ps-product__vendor").innerText.toLowerCase()
            ite_data.prix = produit.querySelector(".ps-product__price.sale").innerText
            allo.push(ite_data)
            })
       return allo
    })
// for(all of allo){
//     const text = 'INSERT INTO jiji(ji_name,ji_prix,ji_image) VALUES($1, $2 ,$3) RETURNING *'
//     const values =[all.namee,all.prix,all.image]
//     pool.query(text, values,(err,res)=>{});
// }
// pool.end()
}
recupDonne()