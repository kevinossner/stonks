import React, { useState, useEffect } from 'react'

const StocksListPage = () => {

    let [stocks, setStocks] = useState([])

    useEffect(() => {
        getStocks()
    }, [])
    let getStocks = async () => {
        let response = await fetch('/api/stocks/')
        let data = await response.json()
        setStocks(data)
    }
    return (
        <div>
            notes
        </div>
    )
}

export default StocksListPage