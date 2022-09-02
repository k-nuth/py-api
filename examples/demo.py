import kth
import signal
import asyncio

running_ = False

def shutdown(sig, frame):
    global running_
    print('Graceful shutdown ...')
    running_ = False

async def main():
    global running_
    signal.signal(signal.SIGINT, shutdown)
    config = kth.config.getDefault(kth.config.Network.mainnet)

    with kth.node.Node(config, True) as node:
        await node.launch(kth.primitives.StartModules.all)
        print("Knuth node has been launched.")
        running_ = True

        (_, height) = await node.chain.getLastHeight()
        print(f"Current height in local copy: {height}")

        if await comeBackAfterTheBCHHardFork(node):
            print("Bitcoin Cash has been created!")

        # node.close()
        print("Good bye!")

async def comeBackAfterTheBCHHardFork(node):
    hfHeight = 478559
    while running_:
        (_, height) = await node.chain.getLastHeight()
        if height >= hfHeight:
            return True
        await asyncio.sleep(10)

    return False

asyncio.run(main())