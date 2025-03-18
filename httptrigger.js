const { TableClient, AzureNamedKeyCredential } = require("@azure/data-tables");

module.exports = async function (context, req) {
    const accountName = process.env.storage_account_name;
    const accountKey = process.env.storage_account_key;
    const tableName = "VisitorCount";

    const credential = new AzureNamedKeyCredential(accountName, accountKey);
    const client = new TableClient(`https://${accountName}.table.core.windows.net`, tableName, credential);

    let visitorCount = 0;

    try {
        const entity = await client.getEntity("Visitor", "Count");
        visitorCount = entity.count || 0;
        visitorCount += 1; 

        await client.updateEntity({
            partitionKey: "Visitor",
            rowKey: "Count",
            count: visitorCount
        }, "Merge");

    } catch (error) {
        await client.createEntity({
            partitionKey: "Visitor",
            rowKey: "Count",
            count: 1
        });

        visitorCount = 1;
    }

    context.res = {
        status: 200,
        body: { count: visitorCount },
        headers: {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*", 
            "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type"
        }
    };
};
